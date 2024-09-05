from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer
from django.urls import reverse
from rest_framework.test import APIClient

class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Author Name')
        self.book = Book.objects.create(
            title='Book Title',
            publication_year=2024,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
    
    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Book')

    def test_get_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        data = {'title': 'Updated Title'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.book.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.list_url, {'title': 'Book Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Book Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_books(self):
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['results'][0]['title'] <= response.data['results'][1]['title'])

    def test_permissions(self):
        # Create a non-authenticated client
        unauthenticated_client = APIClient()
        response = unauthenticated_client.post(self.list_url, {'title': 'Unauthorized Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
