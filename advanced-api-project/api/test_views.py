from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    """

    def setUp(self):
        # Create a user for authenticated actions
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

            # Create authors
        self.author1 = Author.objects.create(name='John Doe')
        self.author2 = Author.objects.create(name='Jane Smith')

        # Create sample books
        self.book1 = Book.objects.create(
            title='Django Basics',
            author=self.author1,
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title='Advanced Python',
            author=self.author2,
            publication_year=2022
        )


    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Django Basics')


    def test_create_book_unauthenticated(self):
        data = {
            'title': 'New Book',
            'author': 'Someone',
            'publication_year': 2023
        }

        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


def test_create_book_unauthenticated(self):
    data = {
        'title': 'New Book',
        'author': self.author1.id,
        'publication_year': 2023
    }

    response = self.client.post('/api/books/create/', data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




    def test_update_book(self):
        self.client.login(username='testuser', password='testpass123')

        data = {
            'title': 'Django Advanced',
            'author': self.author1.id,
            'publication_year': 2021
        }

        response = self.client.put(
            f'/api/books/{self.book1.id}/update/',
            data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Django Advanced')


    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass123')

        response = self.client.delete(
            f'/api/books/{self.book1.id}/delete/'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)



    def test_filter_books_by_year(self):
        response = self.client.get('/api/books/?publication_year=2022')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Advanced Python')



    def test_search_books(self):
        response = self.client.get('/api/books/?search=Django')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django Basics')


    def test_order_books_by_year_desc(self):
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.data[0]['publication_year'], 2022)

