from rest_framework import serializers
from .models import *


class CommentReplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_replies(self, object):
        if object.is_parent:
            replies = Comment.objects.filter(parent=object)
            return CommentReplySerializer(replies, many=True).data
        return None


class CommentListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True, view_name="comments:retrieve_comments", lookup_field="pk"
    )
    user = serializers.StringRelatedField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_replies(self, object):
        if object.is_parent:
            replies = Comment.objects.filter(parent=object)
            return CommentReplySerializer(replies, many=True).data
        return None
