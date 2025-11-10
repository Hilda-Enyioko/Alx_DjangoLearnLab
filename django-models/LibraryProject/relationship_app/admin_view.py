from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from relationship_app.utils import role_required

@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})