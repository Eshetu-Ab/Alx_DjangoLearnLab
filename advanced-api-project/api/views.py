# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    This view handles the creation of a new Book instance.
    Only authenticated users can create a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view handles retrieving, updating, and deleting a Book instance.
    Authenticated users can update or delete a book, while others can only view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]





