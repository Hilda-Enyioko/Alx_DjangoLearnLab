from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

# Generic views for the Book Model

# A ListView for retrieving all books.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # List view should be accessible to for unauthenticated user.
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Add DRF filter functionality
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'published_year']
    search_fields = ['title', 'author']
    ordering_fields = ['published_year', 'title']

# A DetailView for retrieving a single book by ID.
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # List view should be accessible to for unauthenticated user.
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# A CreateView for adding a new book.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Permission check to ensure only authorized and authenticated users can create a book.
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    # Custom behavior to ensure form submission and data validation is handled properly.
    def perform_create(self, serializer):
        
        # Check if data is provided
        if not self.request.data:
            raise ValidationError("No data provided for creating a book.")
        
        # Check if book already exists
        title = self.request.data.get('title')
        if Book.objects.filter(title=title).exists():
            raise ValidationError(f"A book with the title '{title}' already exists.")
        
        serializer.save()

# An UpdateView for modifying an existing book.
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Permission check to ensure only authorized and authenticated users can update a book.
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    # Custom behavior to ensure form submission and data validation is handled properly.
    def perform_update(self, serializer):
        
        # Check if data is provided
        if not self.request.data:
            raise ValidationError("No data provided for updating the book.")
        
        # Check if updating to a title that already exists
        title = self.request.data.get('title')
        if Book.objects.filter(title=title).exclude(pk=self.get_object().pk).exists():
            raise ValidationError(f"A book with the title '{title}' already exists.")
        
        serializer.save()

# A DeleteView for removing a book.
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Permission check to ensure only authorized and authenticated users can delete a book.
    permission_classes = [IsAdminUser, IsAuthenticated]