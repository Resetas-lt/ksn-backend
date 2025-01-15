from rest_framework import serializers

from .models import (
    Post,
)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
