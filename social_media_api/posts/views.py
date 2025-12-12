from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment

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
