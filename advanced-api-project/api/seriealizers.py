# api/serializers.py

from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']




