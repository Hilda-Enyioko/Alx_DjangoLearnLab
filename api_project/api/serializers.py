# A serializer converts model instances into JSON format and vice versa.
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book  
        fields = '__all__'