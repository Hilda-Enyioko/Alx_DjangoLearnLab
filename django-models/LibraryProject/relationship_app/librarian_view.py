# A ‘Librarian’ view accessible only to users identified as ‘Librarians’
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import role_required
from .models import UserProfile

@login_required
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')