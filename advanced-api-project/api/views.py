from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# List all books
class BookListView(generics.ListAPIView):
    """
    This view handles listing all Book instances.
    Allows read-only access to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    This view handles the creation of a new Book instance.
    Only authenticated users can create a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, or delete a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view handles retrieving, updating, and deleting a Book instance.
    Authenticated users can update or delete a book, while others can only view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    This view handles updating an existing Book instance.
    Only authenticated users can update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    This view handles deleting a Book instance.
    Only authenticated users can delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]






