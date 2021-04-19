from rest_framework import serializers

from comments.serializers import *
from .models import *


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many = True, read_only=True)
    user = serializers.StringRelatedField()
    # absolute_url = serializers.SerializerMethodField()
    absolute_url = serializers.HyperlinkedIdentityField(
        view_name="posts:retrieve_post", lookup_field="slug"
    )

    class Meta:
        model = Post
        fields = "__all__"

    # def get_absolute_url(self, object):
    #     return reverse("posts:retrieve_post", kwargs = {'slug': object.slug})


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "created"]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "updated"]
