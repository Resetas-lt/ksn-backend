from django.db import models

from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    content = CKEditor5Field(verbose_name="Turinys")
    show = models.BooleanField(default=True, verbose_name="Rodyti")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Sukurta")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Naujiena"
        verbose_name_plural = "Naujienos"
