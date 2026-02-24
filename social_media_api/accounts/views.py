from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from social_media_api.accounts.models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response(
            {"error": "Invalid Credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid login")

        data['user'] = user

        return data
    


User = get_user_model()


# Follow user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    user_to_follow = get_object_or_404(User, id=user_id)

    request.user.following.add(user_to_follow)

    return Response({
        "message": "User followed"
    })


# Unfollow user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    user_to_unfollow = get_object_or_404(User, id=user_id)

    request.user.following.remove(user_to_unfollow)

    return Response({
        "message": "User unfollowed"
    })