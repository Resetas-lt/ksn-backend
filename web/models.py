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
