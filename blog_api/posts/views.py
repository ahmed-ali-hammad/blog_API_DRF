from rest_framework import generics, views, response
from rest_framework.parsers import MultiPartParser, FormParser
from .pagination import PostPageNumberPagination, PostLimitOffsetPagination
from django.db.models import Q
from rest_framework.permissions import *
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import filters


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'title', 'content']
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            target = queryset.filter(Q(user__username__icontains = query) | 
                Q(title__icontains = query) | 
                Q(content__icontains = query))
            return target
        return queryset


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# class PostRetrieveAPIView(views.APIView):
#     def get(self,request,slug):
#         queryset = Post.objects.get(slug = slug)
#         serializer_class = PostSerializer (queryset)
#         return response.Response (serializer_class.data)

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated, IsOwner]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
