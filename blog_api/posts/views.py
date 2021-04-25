from .pagination import PostPageNumberPagination, PostLimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, views, response
from rest_framework.permissions import *
from rest_framework import filters
from django.db.models import Q
from .serializers import *
from .permissions import *
from .models import *



class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["user__username", "title", "content"]
    pagination_class = PostLimitOffsetPagination

    # custom queryset to apply some custom filters
    def get_queryset(self, *args, **kwargs):
        queryset = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            target = queryset.filter(
                Q(user__username__icontains=query)
                | Q(title__icontains=query)
                | Q(content__icontains=query)
            )
            return target
        return queryset


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# class PostRetrieveAPIView(views.APIView):
#     def get(self,request,slug):
#         queryset = Post.objects.get(slug = slug)
#         serializer_class = PostSerializer (queryset)
#         return response.Response (serializer_class.data)


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated, IsOwner]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    # to get the active user using the request data
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = "slug"
    permission_classes = [IsAuthenticated, IsOwner]
