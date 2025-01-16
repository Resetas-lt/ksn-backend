from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import NewsSerializer


class PostsList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        news_list = Post.objects.all().order_by('-created_at')

        all_posts_serializer = NewsSerializer(news_list, many=True)
        latest_posts_serializer = NewsSerializer(news_list[:4], many=True)

        context = {
            "all_posts": all_posts_serializer.data,
            "latest_posts": latest_posts_serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)
