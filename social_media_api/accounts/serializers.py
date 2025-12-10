from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

User = CustomUser

class UserResgistrationSerializer(serializers.ModelSerializer):
    """
    Docstring for UserResgistrationSerializer:
    Serializer used for creating new user accounts.
    Handles password validation and ensures both password fields match
    """
    
    # The password submitted by user
    password = serializers.CharField(
        writeonly=True,
        required=True,
        validators=[validate_password]
    )
    
    # The second password to match first password
    password2 = serializers.CharField(writeonly=True)
    
    class Meta:
        model = User
        
        # Fields required for user registration
        fields = ['id', 'username', 'email', 'password', 'password2']
        
    def validate(self, attrs):
        """
        Docstring for validate
        Validates that both password and password2 fields match
        Runs before the create() method 
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidateError({
                "password": "Passwords do not match"
            })
             
        return attrs
        
    def create(self, validated_data):
        """
        Docstring for create
        Creates the new user after validation passes
        Removes password2 and uses create_user() so Django handles hashing
        """
        
        validated_data.pop('password2')             # Remove the unnecessary field
        
        # create user automatically hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get['email'],
            password=validate_password['password']
        )
        
        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()