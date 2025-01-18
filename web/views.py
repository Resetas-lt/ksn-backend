from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.core.mail import send_mail

from email.utils import formataddr


from .models import Post
from .serializers import PostSerializer


class ContactusView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        print(data)

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
