# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authenticated tests
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        
        # Create an author
        self.author = Author.objects.create(name="Author A")

        # Create sample books with proper author instance
        self.book1 = Book.objects.create(
            title="Alpha Book",
            author=self.author,
            publication_year=2025
        )

        self.book2 = Book.objects.create(
            title="Beta Book",
            author=self.author,
            publication_year=2025
        )
        
        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.book_id])

    # ---------- LIST TEST ----------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ---------- CREATE TEST ----------
    def test_create_book(self):
        data = {"title": "New Book", "author": "New Author"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ---------- RETRIEVE TEST ----------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")

    # ---------- UPDATE TEST ----------
    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Author A"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    # ---------- DELETE TEST ----------
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTER TEST ----------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + "?search=Alpha")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    # ---------- AUTHENTICATION TEST ----------
    def test_unauthenticated_user_cannot_create_book(self):
        unauth_client = APIClient()  # Not logged in
        data = {"title": "Blocked Book", "author": "Nobody"}
        response = unauth_client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
