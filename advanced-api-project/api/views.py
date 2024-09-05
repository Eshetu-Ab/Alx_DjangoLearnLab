# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .seriealizers import BookSerializer
from .permissions import IsAdminUser

class BookListView(generics.ListCreateAPIView):
    """
    Retrieve all books or create a new book.
    - GET: List all books.
    - POST: Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUser]  # Example of using custom permission

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific book by ID.
    - GET: Retrieve a book.
    - PUT/PATCH: Update a book.
    - DELETE: Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




