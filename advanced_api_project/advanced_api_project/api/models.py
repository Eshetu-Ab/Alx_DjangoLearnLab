from django.db import models

# The Author model represents an author who can have multiple books associated with them.
# This model contains only one field:
# - name: A CharField to store the author's name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# The Book model represents a book that is associated with an author.
# Fields:
# - title: A CharField to store the title of the book.
# - publication_year: An IntegerField to store the year the book was published.
# - author: A ForeignKey linking to the Author model, establishing a one-to-many relationship (one author can have many books).
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


