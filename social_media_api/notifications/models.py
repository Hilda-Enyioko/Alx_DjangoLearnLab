from django.db import models
from accounts.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Notification(models.Model):
    # recipient is the user who receives the notification
    recipient = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='received_notifications'
    )
    
    # actor is the user who triggers the notification
    actor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sent_notifications'
    )
    
    verb = models.CharField(max_length=255)  # describing the action e.g., 'liked', 'commented on'
    
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('content_type', 'object_id')  # can point to any model instance
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Notification for {self.recipient.username} - {self.verb} by {self.actor.username}"