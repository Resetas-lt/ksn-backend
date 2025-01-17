from django.contrib import admin

from .models import (
    Post,
    PostImage,
)


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'show', 'slug', 'created_at')
    list_filter = ['show', 'created_at']
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
