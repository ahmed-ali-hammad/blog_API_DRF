from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from posts.models import *
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete = models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    @property
    def is_parent(self):
        if self.parent == None:
            return True
        return False
