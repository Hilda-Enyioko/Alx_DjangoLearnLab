# An ‘Admin’ view that only users with the ‘Admin’ role can access
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import role_required

@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')