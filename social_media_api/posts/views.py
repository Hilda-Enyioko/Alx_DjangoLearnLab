from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment, Like
from notifications.models import Notification

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    
    # Inline pagination class
    class PostPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 50
        
    pagination_class = PostPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Inline pagination class
    class CommentPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 50
    
    pagination_class = CommentPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.CreateAPIView):
    """
    Allows a user to like a post
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        
        # Prevent duplicate likes
        like, created = Like.objects.get_or_create(post=post, liked_by=request.user)
        if not created:
            return Response(
                {"error": "You have already liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )
    
        # Notify Post Author of Like
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
                      
        return Response(
            {'message': 'Post liked successfully'}, 
            status=status.HTTP_201_CREATED
        )


class UnlikePostView(generics.DestroyAPIView):
    """
    Allows a user to unlike a post
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        
        like = Like.objects.filter(post=post, liked_by=request.user).first()
        if not like:
            return Response(
                {"error": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        like.delete()
        
        return Response(
            {'message': 'Post unliked successfully'}, 
            status=status.HTTP_200_OK
        )