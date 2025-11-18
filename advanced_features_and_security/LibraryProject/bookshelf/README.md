# Permissions and Groups

- Custom permissions defined in Book model: can_view, can_create, can_edit, can_delete
- Groups:
    - Viewers: can_view
    - Editors: can_create, can_edit
    - Admins: all permissions
- Views use @permission_required decorator to enforce permissions.
- Groups and permissions are automatically created using signals.
