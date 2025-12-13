from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from notifications.views import create_notification

from .models import User as CustomUser
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer
)


class RegisterView(generics.CreateAPIView):
    """
    Handles user registration
    """
    serializer_class = UserRegistrationSerializer


class LoginView(APIView):
    """
    Handles user login and token generation
    """
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Login successful",
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })


class FollowUserView(generics.GenericAPIView):
    """
    Allows a user to follow another user
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if request.user == user_to_follow:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)
        
        create_notification(
                recipient=user_to_follow,
                actor=request.user,
                verb="started following you",
                message=f"{request.user.username} started following you."
            )

        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    """
    Allows a user to unfollow another user
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if user_to_unfollow not in request.user.following.all():
            return Response(
                {"error": f"You do not follow this account, {user_to_unfollow.username}."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": f"You have unfollowed {user_to_unfollow.username}."},
            status=status.HTTP_200_OK
        )


class ListFollowingView(generics.ListAPIView):
    """
    Lists users the current user is following
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.following.all()


class ListFollowersView(generics.ListAPIView):
    """
    Lists users who follow the current user
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.followers.all()

class TestAuthView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "message": "Token auth works!"
        })