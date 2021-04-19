from rest_framework import generics
from rest_framework.permissions import *
from posts.permissions import *
from posts.pagination import *
from .serializers import *


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostLimitOffsetPagination


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
