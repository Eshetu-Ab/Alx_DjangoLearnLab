from django.db import models

# One-to-One relationship example: Each Author has one Profile
class Profile(models.Model):
    bio = models.TextField()
    birthdate = models.DateField()
    
    def __str__(self):
        return f"Profile {self.id}"

# Many-to-Many relationship example: An Author can write multiple Books, and a Book can have multiple Authors
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='author')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='books')
    
    def __str__(self):
        return self.title

# ForeignKey example: A Book belongs to a Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title

