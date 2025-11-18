# advanced_features_and_security/library_app/signals.py

from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate

def create_groups(sender, **kwargs):
    content_type = ContentType.objects.get(app_label='library_app', model='book')

    # Define permissions
    can_view = Permission.objects.get(codename='can_view', content_type=content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

    # Create groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    # Assign permissions
    editors.permissions.set([can_create, can_edit])
    viewers.permissions.set([can_view])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])

class LibraryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library_app'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)
