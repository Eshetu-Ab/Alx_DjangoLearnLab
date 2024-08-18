from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters to the right side of the list view
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')

