# Django REST Framework API: Authentication & Permissions Documentation

## Overview
This API uses Django REST Framework (DRF) to manage authentication and permissions.

- **Authentication** ensures that a user is who they claim to be.
- **Permissions** control what authenticated (or unauthenticated) users are allowed to do.

DRF supports:
- TokenAuthentication
- SessionAuthentication
- JWTAuthentication (via third-party packages)

Common permission classes:
- `IsAuthenticated` – Only logged-in users can access.
- `IsAdminUser` – Only admin users can access.
- `AllowAny` – Anyone, including anonymous users, can access.
- Custom permissions – You can define your own rules.

