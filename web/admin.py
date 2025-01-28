from django.contrib import admin

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
    inlines = [BudgetReportFileInline]
    list_display = ('title', 'created_at')
    search_fields = ['title']


class FinancesReportAdmin(admin.ModelAdmin):
    inlines = [FinancesReportFileInline]
    list_display = ('title', 'created_at')
    search_fields = ['title']


class SalaryReportAdmin(admin.ModelAdmin):
    inlines = [SalaryReportFileInline]
    list_display = ('title', 'created_at')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(EmployeeContact, EmployeeContactAdmin)
admin.site.register(BudgetReport, BudgetReportAdmin)
admin.site.register(FinancesReport, FinancesReportAdmin)
admin.site.register(SalaryReport, SalaryReportAdmin)
