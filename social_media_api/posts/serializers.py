from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    """
    Docstring for CommentSerializer
    Serailizer for creating and retrieving comments
    """
    
    author = serializers.CharField(source="author.username", read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = '__all__'
    
    def validate_content(self, value):
        """
        Docstring for validate_content
        Prevent empty comments
        """
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value
    

class PostSerializer(serializers.ModelSerializer):
    """
    Docstring for PostSerializer
    Serializer for creating and retrieing posts
    """
    
    author = serializers.CharField(source="author.username", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'