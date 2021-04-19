from django.urls import path
from .views import *

app_name = "comments"

urlpatterns = [
    path("list/", CommentListAPIView.as_view(), name="list_comments"),
    path(
        "detail/<int:pk>/", CommentRetrieveAPIView.as_view(), name="retrieve_comments"
    ),
]
