from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and retrieving comments
    """

    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

    def validate_content(self, value):
        """Prevent empty comments"""
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and retrieving posts
    """

    author = serializers.CharField(source="author.username", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'comments']
