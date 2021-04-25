from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models
from posts.models import *


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # generic foreignkey settings to connect the Comment model to any other models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    # to give an option for replies to a certain comment
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    # a method to check if the instance is a comment or a reply
    @property
    def is_parent(self):
        if self.parent == None:
            return True
        return False
