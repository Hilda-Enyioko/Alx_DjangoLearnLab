# A ‘Member’ view for users with the ‘Member’ role
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .utils import role_required

@login_required
@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')