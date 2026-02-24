from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "password"]


    def create(self, validated_data):

        user = get_user_model().objects.create_user(

            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],

        )

        Token.objects.create(user=user)

        return user



# Login Serializer
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(write_only=True)


    def validate(self, data):

        user = authenticate(

            username=data["username"],
            password=data["password"]

        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user

        return data