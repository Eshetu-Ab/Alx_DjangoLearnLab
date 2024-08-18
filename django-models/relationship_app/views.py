from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from .models import Book


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class BookListView(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'





