# api/urls.py

from django.urls import path
from .views import BookCreateView, BookDetailView

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]

