from django.urls import path, include
from .views import *

app_name = "posts"

urlpatterns = [
    path("list/", PostListAPIView.as_view(), name="list_posts"),
    path("create/", PostCreateAPIView.as_view(), name="Create_post"),
    path("detail/<slug:slug>/", PostRetrieveAPIView.as_view(), name="retrieve_post"),
    path("update/<slug:slug>/", PostUpdateAPIView.as_view(), name="update_post"),
    path("delete/<slug:slug>/", PostDeleteAPIView.as_view(), name="delete_post"),
]
