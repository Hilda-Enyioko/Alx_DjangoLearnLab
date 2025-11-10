from atexit import register
from django.urls import path
from .views import UserLoginView, UserLogoutView, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication routes
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]