from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.core.mail import send_mail

from email.utils import formataddr


from .models import (
    Post,
    EmployeeContact,
    BudgetReport,
    FinancesReport,
    SalaryReport,
    Project,
)
from .serializers import (
    PostSerializer,
    EmployeeContactSerializer,
    BudgetReportSerializer,
    FinancesReportSerializer,
    SalaryReportSerializer,
    ProjectSerializer,
)


class ContactusView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        firstname = data.get("firstname")
        email = data.get("email")
        message = data.get("message")

        message_format = f"Vardas: {firstname}\nEl. paštas: {email}\n\n{message}"

        subject = "Nauja žinutė iš kontaktų formos"

        try:
            send_mail(
                subject=subject,
                message=message_format,
                from_email=formataddr(
                    ("KSN.LT", email)),
                recipient_list=["web@ksn.lt"],
                fail_silently=False,
            )
            return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Failed to send message!"}, status=status.HTTP_400_BAD_REQUEST)


class PostsList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        news_list = Post.objects.filter(show=True).order_by('-created_at')

        all_posts_serializer = PostSerializer(
            news_list, many=True, context={"request": request})
        latest_posts_serializer = PostSerializer(
            news_list[:4], many=True, context={"request": request})

        context = {
            "all_posts": all_posts_serializer.data,
            "latest_posts": latest_posts_serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)


class PostDetails(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        serializer = PostSerializer(post, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        contacts = EmployeeContact.objects.filter(show=True).order_by('id')

        serializer = EmployeeContactSerializer(contacts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BudgetReportList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reports = BudgetReport.objects.all().order_by('-created_at')

        serializer = BudgetReportSerializer(
            reports, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class FinancesReportList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reports = FinancesReport.objects.all().order_by('-created_at')

        serializer = FinancesReportSerializer(
            reports, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class SalaryReportList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reports = SalaryReport.objects.all().order_by('-created_at')

        serializer = SalaryReportSerializer(
            reports, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = Project.objects.all().order_by('id')

        serializer = ProjectSerializer(
            projects, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
