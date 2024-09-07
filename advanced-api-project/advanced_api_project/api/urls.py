from django.urls import path
from .views import (
    BookListView, 
    BookCreateView, 
    BookDetailView, 
    BookUpdateView, 
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete an existing book
]


