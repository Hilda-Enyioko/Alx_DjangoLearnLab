from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics, permissions
from .serializers import NotificationSerializer
from .models import Notification

# Create your views here.
"""
Notification Handling:
 - Set up views and methods to create notifications whenever relevant actions occur, such as a user getting a new follower, someone liking their post, or commenting on their post.
- Provide an endpoint for users to fetch their notifications, showcasing unread notifications prominently.
"""

def create_notification(recipient, actor, verb, target=None):
    if recipient == actor:
        # Don't notify yourself
        return
    
    content_type = None
    object_id = None
    
    if target:
        content_type = ContentType.objects.get_for_model(target)
        object_id = target.id
    
    notification = Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target=target,
        content_type=content_type,
        object_id=object_id
    )
    return notification


class NotificationListView(generics.ListAPIView):
    """
    Lists notifications for the authenticated user
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('read','-timestamp')
    

class MarkNotificationAsReadView(generics.UpdateAPIView):
    """
    Marks a notification as read
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def get_object(self):
        notification = super().get_object()
        if notification.recipient != self.request.user:
            raise PermissionDenied("You do not have permission to modify this notification.")
        return notification

    def perform_update(self, serializer):
        serializer.save(read=True)