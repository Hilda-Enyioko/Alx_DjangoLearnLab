from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import CustomUser

# Create your views here.
class RegisterView(generics.CreateAPIView):
    """
    Docstring for RegisterView
    Handles user registration
    """
    
    serializer_class=UserResgistrationSerializer
    

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
