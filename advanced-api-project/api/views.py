from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

class BookListView(generics.ListCreateAPIView):
    """
    View to list all books or create a new book.
    - GET: List all books.
    - POST: Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a book instance.
    - GET: Retrieve a book.
    - PUT/PATCH: Update a book.
    - DELETE: Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



