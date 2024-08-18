from django.urls import path
from .views import list_books
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', list_books, name='list_books'),
]

urlpatterns = [
    path('books/', BookListView.as_view(), name='list_books'),
]
