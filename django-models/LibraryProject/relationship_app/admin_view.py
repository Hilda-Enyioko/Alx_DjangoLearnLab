# An ‘Admin’ view that only users with the ‘Admin’ role can access
from django.contrib import admin
from django.shortcuts import render
from .utils import login_required

@role_required('Admin')
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')