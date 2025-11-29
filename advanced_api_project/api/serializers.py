# Custom Serializers for the API app
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

"""
Book Serializer:
This serializer handles the serialization and deserialization of Book instances from the Book model.
This means that it converts Book model instances to JSON format and vice versa for API interactions.
It includes all fields of the Book model.
Additionally, it has custom validation to ensure that the publication_year is not set in the future.
This is done by overriding the validate_publication_year method which checks the year against the current year.
"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    # custom validation for publication_year
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

"""
Author Serializer:
This serializer handles the serialization and deserialization of Author instances from the Author model.
It includes all fields of the Author model.
It also includes a nested representation of the books written by the author using the BookSerializer.
This is achieved by defining a books field that uses BookSerializer with many=True to indicate multiple related instances.
However, the books field is read-only, meaning it cannot be used to create or update books through the Author serializer.
"""       
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['author_id', 'name', 'email', 'books']