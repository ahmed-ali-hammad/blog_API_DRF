from django.contrib import admin

from django.contrib.contenttypes.admin import GenericTabularInline

from comments.models import *

from .models import *


class CommentTabularInline(GenericTabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentTabularInline]


admin.site.register(Post, PostAdmin)

admin.site.register(Comment)