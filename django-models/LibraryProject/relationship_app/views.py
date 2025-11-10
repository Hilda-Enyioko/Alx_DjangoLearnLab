from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import Book
from .models import Library

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Show library details and books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# User Login View
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    
# User Logout View 
class UserLogoutView(LogoutView):
    next_page = 'login'
    template_name = 'relationship_app/logout.html'

# User Registration View
def register(request):
    if request.method == 'POST': # user submitted the form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})