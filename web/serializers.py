from rest_framework import serializers

from django.conf import settings

from .models import (
    Post,
    PostImage,
    EmployeeContact,
)


class AbsoluteImageUrlField(serializers.ImageField):
    def to_representation(self, value):
        request = self.context.get('request')
        if not value:
            return None
        if request is not None:
            return request.build_absolute_uri(value.url)
        return value.url


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    thumbnail = AbsoluteImageUrlField()
    images = PostImageSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        """Modify the `content` field to include full media URLs."""
        representation = super().to_representation(instance)
        if 'content' in representation and representation['content']:
            representation['content'] = self.add_full_media_url(
                representation['content'])
        return representation

    def add_full_media_url(self, content):
        """Replace relative media URLs with absolute URLs."""
        media_url = settings.MEDIA_URL
        full_media_url = f"{settings.SITE_URL}{media_url}"
        return content.replace(media_url, full_media_url)


class EmployeeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeContact
        fields = "__all__"
