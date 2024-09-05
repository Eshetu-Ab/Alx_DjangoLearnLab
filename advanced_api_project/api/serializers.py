from rest_framework import serializers
from .models import Author, Book
from datetime import date

# The BookSerializer is responsible for serializing the Book model.
# It includes all the fields of the Book model.
# Custom validation is added to ensure the publication_year is not set to a future year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for the publication_year field
    # This method ensures that the publication year cannot be in the future.
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# The AuthorSerializer is responsible for serializing the Author model.
# In addition to the name field, it also includes a nested BookSerializer to serialize related books.
# This allows us to retrieve all books written by the author in a nested format.
class AuthorSerializer(serializers.ModelSerializer):
    # The books field is a nested serializer that serializes all related books.
    # The many=True argument indicates that an author can have multiple books.
    # The read_only=True argument ensures that the books are read-only and won't be used for creating/updating authors.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

