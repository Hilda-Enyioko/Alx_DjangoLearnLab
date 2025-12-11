from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Docstring for IsOwnerOrReadOnly
    Custom Permissions:
    - SAFE METHODS (GET, HEAD, OPTIONS): allowed for everyone
    - POST, PUT, PATCH, DELETE: only allowed for the object owner
    """
    
    def has_object_permssion(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user