from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    """
    Decorator for views that checks whether a user has a specific role.
    Assumes that the UserProfile model is linked to the User model via a OneToOneField.
    """
    def check_role(user):
        if not user.is_authenticated:
            return False
        try:
            return user.userprofile.role == role
        except UserProfile.DoesNotExist:
            return False

    return user_passes_test(check_role)