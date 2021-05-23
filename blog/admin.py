from django.db import models
from django.contrib import admin
from blog.models import post


# Register your models here.


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_at", "status"]
    list_filter = ["status", "created_at", "published_at", "author"]
    search_fields = ["title", "content"]
    raw_id_fields = [
        "author",
    ]
    date_hierarchy = "published_at"
    ordering = ["status", "published_at"]
