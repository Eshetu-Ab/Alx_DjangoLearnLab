from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter




# BookListView handles retrieving a list of all books and creating new books.
# - GET: Retrieves a list of all books in the database.
# - POST: Allows authenticated users to create a new book.
#   - This endpoint is accessible to all users.


# BookListView supports filtering by title, author, and publication year.
# It also supports searching by title and author name.
# Ordering can be done by title or publication year.


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']  # Fields that can be used for ordering
    ordering = ['title']  # Default ordering




    def perform_create(self, serializer):
        # Custom logic before saving a new book can be added here.
        serializer.save()

# BookDetailView handles retrieving, updating, and deleting a specific book by ID.
# - GET: Retrieves details of a specific book by its ID.
# - PUT: Allows authenticated users to update the book’s details.
# - DELETE: Allows authenticated users to delete the book.
#   - This view is restricted to authenticated users only.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view.


    


   
