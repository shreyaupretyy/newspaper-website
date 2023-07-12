from django.contrib import admin
from django.db import models
from .models import Articles, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Articles, ArticleAdmin)
admin.site.register(Comment)
