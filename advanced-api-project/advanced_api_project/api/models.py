from django.db import models

class Author(models.Model):
   """
    The Author model represents a writer of books. Each author can write multiple books,
    hence the one-to-many relationship between Author and Book.

    """
    
   name = models.CharField(max_length=100) 

   def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
