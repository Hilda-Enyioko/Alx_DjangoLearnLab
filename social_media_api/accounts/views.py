from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from .models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    """
    Docstring for RegisterView
    Handles user registration
    """
    
    serializer_class=UserRegistrationSerializer
    

class LoginView(APIView):
    """
    Docstring for LoginView
    Hangles user login and token generation
    """
    serializer_class = UserLoginSerializer
    
    def post(self, request):
        # Validate incoming login data (username & password)
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract validated username and password
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        # Authenticate user (checks username, password, and returns associated user object)      
        user = authenticate(username=username, password=password)
        
        # If authentication failed
        if not user:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Generate or retrieve authentication token for the validated user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return successful response with token and user details
        return Response({
            "message": "Login successful",
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })
        
        
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        
        if request.user == user_to_follow:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request.user.following.add(user_to_follow)
        
        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )
        

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        
        if user_to_unfollow not in request.user.following.all():
            return Response(
                {"error": f"You do not follow this acoount, {user_to_unfollow.username}."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request.user.following.remove(user_to_unfollow)
        
        return Response(
            {"message": f"You have unfollowed {user_to_unfollow.username}."}
        )
        

class ListFollowingView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        following = request.user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)
    

class ListFollowersView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        followers = request.user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)