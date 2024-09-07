from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from rest_framework.permissions import IsAuthenticated

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create test authors and books
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2024,
            author=self.author
        )
    
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')
    
    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        data = {
            'title': 'Updated Book Title'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book Title')
    
    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books_filtering(self):
        url = reverse('book-list') + '?title=Test Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_list_books_search(self):
        url = reverse('book-list') + '?search=Test Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_list_books_ordering(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['results'][0]['publication_year'] <= response.data['results'][1]['publication_year'])

    def test_permissions(self):
        # Test read-only access for unauthenticated users
        self.client.logout()
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test authenticated access for create, update, and delete
        url = reverse('book-list')
        response = self.client.post(url, {'title': 'Another Book', 'publication_year': 2025, 'author': self.author.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.patch(url, {'title': 'Yet Another Book Title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
