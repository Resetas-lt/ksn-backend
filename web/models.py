from django.db import models
from django.utils.text import slugify

from django_ckeditor_5.fields import CKEditor5Field

import itertools


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    description = models.TextField(
        blank=True, null=True, verbose_name="Trumpas aprašymas")
    content = CKEditor5Field(verbose_name="Turinys")
    thumbnail = models.ImageField(
        upload_to="news_thumbnails", blank=True, null=True, verbose_name="Nuotrauka")
    show = models.BooleanField(default=True, verbose_name="Rodyti")
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Sukurta")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            for x in itertools.count(1):
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{slugify(self.title)}-{x}'
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Naujiena"
        verbose_name_plural = "Naujienos"


class PostImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="news_images",
                              verbose_name="Nuotrauka")

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = "Nuotrauka"
        verbose_name_plural = "Nuotraukos"


class EmployeeContact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Darbuotojas")
    division = models.CharField(max_length=100, verbose_name="Skyrius")
    position = models.CharField(max_length=100, verbose_name="Pareigos")
    phone = models.CharField(max_length=100, verbose_name="Telefonas")
    email = models.EmailField(max_length=100, verbose_name="El. paštas")
    show = models.BooleanField(default=True, verbose_name="Rodyti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kontaktas"
        verbose_name_plural = "Kontaktai"


class BudgetReport(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Sukurta")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "biudžeto ataskaita"
        verbose_name_plural = "biudžeto ataskaitos"


class BudgetQuarter(models.Model):
    report = models.ForeignKey(
        BudgetReport, null=True, on_delete=models.CASCADE, related_name="quarters", verbose_name="Ataskaita")
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Biudžeto ketvirtis"
        verbose_name_plural = "Biudžeto ketvirčiai"


class BudgetReportFile(models.Model):
    quarter = models.ForeignKey(
        BudgetQuarter, null=True, on_delete=models.CASCADE, related_name="files", verbose_name="Ketvirtis")
    file = models.FileField(upload_to="budget_reports",
                            verbose_name="Failas")

    def __str__(self):
        return self.quarter.title

    class Meta:
        verbose_name = "Failas"
        verbose_name_plural = "Failai"


class FinancesReport(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Sukurta")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Finansų ataskaita"
        verbose_name_plural = "Finansų ataskaitos"


class FinancesQuarter(models.Model):
    report = models.ForeignKey(
        FinancesReport, null=True, on_delete=models.CASCADE, related_name="quarters", verbose_name="Ataskaita")
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Finansų ketvirtis"
        verbose_name_plural = "Finansų ketvirčiai"


class FinancesReportFile(models.Model):
    quarter = models.ForeignKey(
        FinancesQuarter, null=True, on_delete=models.CASCADE, related_name="files", verbose_name="Ketvirtis")
    file = models.FileField(upload_to="finances_reports",
                            verbose_name="Failas")

    def __str__(self):
        return self.quarter.title

    class Meta:
        verbose_name = "Failas"
        verbose_name_plural = "Failai"


class SalaryReport(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Sukurta")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Atlyginimų ataskaita"
        verbose_name_plural = "Atlyginimų ataskaitos"


class SalaryQuarter(models.Model):
    report = models.ForeignKey(
        SalaryReport, null=True, on_delete=models.CASCADE, related_name="quarters", verbose_name="Ataskaita")
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Atlyginimų ketvirtis"
        verbose_name_plural = "Atlyginimų ketvirčiai"


class SalaryReportFile(models.Model):
    quarter = models.ForeignKey(
        SalaryQuarter, null=True, on_delete=models.CASCADE, related_name="files", verbose_name="Ketvirtis")
    file = models.FileField(upload_to="salary_reports",
                            verbose_name="Failas")

    def __str__(self):
        return self.quarter.title

    class Meta:
        verbose_name = "Failas"
        verbose_name_plural = "Failai"


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Pavadinimas")
    description = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Aprašymas")
    thumbnail = models.ImageField(
        upload_to="project_thumbnails", blank=True, null=True, verbose_name="Nuotrauka")
    project_id = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Projekto ID")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"


class ProjectFile(models.Model):
    project = models.ForeignKey(
        Project, null=True, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="project_files", null=True,
                            verbose_name="Failas")

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = "Projekto failas"
        verbose_name_plural = "Projektų failai"


class Rating(models.Model):
    RATING_CHOICES = [
        ('perfect', 'Puikiai'),
        ('good', 'Gerai'),
        ('decent', 'Patenkinamai'),
        ('bad', 'Blogai'),
    ]

    ip_address = models.GenericIPAddressField(
        null=True, blank=True, verbose_name="Balsuotojo IP")
    rating = models.CharField(
        max_length=100, choices=RATING_CHOICES, verbose_name="Įvertinimas")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Sukurta")

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = "Įvertinimas"
        verbose_name_plural = "Įvertinimai"
