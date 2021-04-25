from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register_user"),
    path("login/", UserLoginAPIView.as_view(), name="login_user"),
]
