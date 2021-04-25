from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Q


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="Email Address")
    email2 = serializers.EmailField(label="Confirm Email")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "email2",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data["email"]
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("this user has already registered.")
        return data

    def validate_email2(self, value):
        data = self.get_initial()
        email = data.get("email")
        email2 = value
        if email != email2:
            raise serializers.ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        label="Email Address", required=False, allow_blank=True
    )
    username = serializers.CharField(required=False, allow_blank=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data["username"]
        email = data["email"]
        password = data["password"]

        if not email and not username:
            raise serializers.ValidationError(
                "Please enter a valid email or a username."
            )

        try:
            user = User.objects.filter(username=username)
        except:
            user = user.objects.filter(email=email)

        if user.exists() and user.count() == 1:
            user_obj = user[0]
        else:
            raise serializers.ValidationError("User doesn't exist.")

        authenticated_user = authenticate(username=user_obj.username, password=password)
        if authenticated_user == None:
            raise serializers.ValidationError(
                "incorrect credentials, please try again."
            )
        data = {
            "username": user_obj.username,
            "email": user_obj.email,
            "token": "some random token",
        }

        return data