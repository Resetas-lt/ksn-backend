from rest_framework import serializers

from django.conf import settings

from .models import (
    Post,
    PostImage,
    EmployeeContact,
    BudgetReport,
    BudgetReportFile,
    FinancesReport,
    FinancesReportFile,
    SalaryReport,
    SalaryReportFile,
    Project,
    ProjectFile,
)

import os


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


class BudgetReportFileSerializer(serializers.ModelSerializer):
    file = AbsoluteImageUrlField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = BudgetReportFile
        fields = "__all__"

    def get_name(self, obj):
        return os.path.basename(obj.file.name)


class BudgetQuarterSerializer(serializers.ModelSerializer):
    files = BudgetReportFileSerializer(many=True, read_only=True)

    class Meta:
        model = BudgetReport
        fields = "__all__"


class BudgetReportSerializer(serializers.ModelSerializer):
    quarters = BudgetQuarterSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = BudgetReport
        fields = "__all__"


class FinancesReportFileSerializer(serializers.ModelSerializer):
    file = AbsoluteImageUrlField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = FinancesReportFile
        fields = "__all__"

    def get_name(self, obj):
        return os.path.basename(obj.file.name)


class FinancesQuarterSerializer(serializers.ModelSerializer):
    files = FinancesReportFileSerializer(many=True, read_only=True)

    class Meta:
        model = FinancesReport
        fields = "__all__"


class FinancesReportSerializer(serializers.ModelSerializer):
    quarters = FinancesQuarterSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = FinancesReport
        fields = "__all__"


class FinancesQuarterSerializer(serializers.ModelSerializer):
    files = FinancesReportFileSerializer(many=True, read_only=True)

    class Meta:
        model = FinancesReport
        fields = "__all__"


class SalaryReportFileSerializer(serializers.ModelSerializer):
    file = AbsoluteImageUrlField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = SalaryReportFile
        fields = "__all__"

    def get_name(self, obj):
        return os.path.basename(obj.file.name)


class SalaryQuarterSerializer(serializers.ModelSerializer):
    files = SalaryReportFileSerializer(many=True, read_only=True)

    class Meta:
        model = SalaryReport
        fields = "__all__"


class SalaryReportSerializer(serializers.ModelSerializer):
    quarters = SalaryQuarterSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = SalaryReport
        fields = "__all__"


class ProjectFileSerializer(serializers.ModelSerializer):
    file = AbsoluteImageUrlField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = ProjectFile
        fields = "__all__"

    def get_name(self, obj):
        return os.path.basename(obj.file.name)


class ProjectSerializer(serializers.ModelSerializer):
    thumbnail = AbsoluteImageUrlField()
    files = ProjectFileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
