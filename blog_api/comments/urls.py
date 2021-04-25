from django.urls import path
from .views import *

app_name = "comments"

urlpatterns = [
    path("list/", CommentListAPIView.as_view(), name="list_commenst"),
    path("create/", commentCreateAPIView.as_view(), name="create_comment"),
    path("detail/<int:pk>/", CommentRetrieveAPIView.as_view(), name="retrieve_comment"),
    path("update/<int:pk>/", commentUpdateAPIView.as_view(), name="update/delete_comment"),
]
