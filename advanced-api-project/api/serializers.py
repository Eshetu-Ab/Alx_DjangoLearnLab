from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
     """
     The AuthorSerializer serializes the Author model and includes a nested BookSerializer 
    to represent all related books for that author.
    """




     books = BookSerializer(many=True, read_only=True)

     class Meta:
        model = Author
        fields = ['name', 'books']
