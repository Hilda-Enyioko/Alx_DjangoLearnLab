from . import views
from django.urls import path
from .views import UserLoginView, UserLogoutView, list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Role-based views
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    # Permission-based views
    path('add_book/', add_book, name="add_book"),
    path('edit_book/', edit_book, name="edit_book"),
    path('delete_book/', delete_book, name="delete_book")
]