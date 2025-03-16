from django.contrib import admin

from .models import (
    Post,
    PostImage,
    EmployeeContact,
    BudgetReport,
    BudgetQuarter,
    BudgetReportFile,
    FinancesReport,
    FinancesQuarter,
    FinancesReportFile,
    SalaryReport,
    SalaryQuarter,
    SalaryReportFile,
    Project,
    ProjectFile,
    Car,
    TenderReport,
    TenderFile,
    Rating,
)


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class BudgetReportFileInline(admin.TabularInline):
    model = BudgetReportFile
    extra = 1


class FinancesReportFileInline(admin.TabularInline):
    model = FinancesReportFile
    extra = 1


class SalaryReportFileInline(admin.TabularInline):
    model = SalaryReportFile
    extra = 1


class ProjectFileInline(admin.TabularInline):
    model = ProjectFile
    extra = 1


class TenderFileInline(admin.TabularInline):
    model = TenderFile
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'show', 'slug', 'created_at')
    list_filter = ['show', 'created_at']
    search_fields = ['title', 'content']


class EmployeeContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'position', 'phone', 'email', 'show')
    list_filter = ['show']
    search_fields = ['name', 'division', 'position', 'phone', 'email']


class BudgetReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']


class BudgetQuarterAdmin(admin.ModelAdmin):
    inlines = [BudgetReportFileInline]
    list_display = ('report', 'title')
    search_fields = ['title']


class FinancesReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']


class FinancesQuarterAdmin(admin.ModelAdmin):
    inlines = [FinancesReportFileInline]
    list_display = ('report', 'title')
    search_fields = ['title']


class SalaryReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']


class SalaryQuarterAdmin(admin.ModelAdmin):
    inlines = [SalaryReportFileInline]
    list_display = ('report', 'title')
    search_fields = ['title']


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectFileInline]
    list_display = ('title', 'description', 'thumbnail',
                    'project_id')
    search_fields = ('title', 'description', 'project_id')


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')
    search_fields = ['make', 'model', 'year']


class TenderReportAdmin(admin.ModelAdmin):
    inlines = [TenderFileInline]
    list_display = ('title', 'created_at')
    search_fields = ['title']


class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'rating', 'created_at')
    search_fields = ['rating']


admin.site.register(Post, PostAdmin)
admin.site.register(EmployeeContact, EmployeeContactAdmin)
admin.site.register(BudgetReport, BudgetReportAdmin)
admin.site.register(BudgetQuarter, BudgetQuarterAdmin)
admin.site.register(FinancesReport, FinancesReportAdmin)
admin.site.register(FinancesQuarter, FinancesQuarterAdmin)
admin.site.register(SalaryReport, SalaryReportAdmin)
admin.site.register(SalaryQuarter, SalaryQuarterAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(TenderReport, TenderReportAdmin)
admin.site.register(Rating, RatingAdmin)
