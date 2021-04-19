from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PostPageNumberPagination(PageNumberPagination):
    page_size = 8


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 8