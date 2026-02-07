from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Accessible to everyone (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]



class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book using its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

