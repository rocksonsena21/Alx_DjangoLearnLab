from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class Listview(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Detailview(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Createview(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Updateview(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Deleteview(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

