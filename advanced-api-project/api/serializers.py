from rest_framework import serializers
from .models import Author, Book
import datetime  # Import the datetime module

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, including validation for publication_year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model, including nested BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']



