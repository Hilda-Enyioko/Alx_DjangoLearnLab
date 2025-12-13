from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.CharField(source="recipient.username", read_only=True)
    actor = serializers.CharField(source="actor.username", read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'timestamp', 'read']