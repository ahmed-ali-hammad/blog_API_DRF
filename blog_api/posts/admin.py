from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from comments.models import *
from .models import *

# this setting is to show the comments along with the post on a single screen in the admin panel
class CommentTabularInline(GenericTabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentTabularInline]


admin.site.register(Post, PostAdmin)
