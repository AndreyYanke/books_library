from django.shortcuts import render
from rest_framework import generics

from booksapp.models import Book, Author
from booksapp.serializers import BooksListSerializer, AuthorListSerializer


class BooksListView(generics.ListAPIView):
    """Вывод списка книг"""
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer


class  AuthorListView(generics.ListAPIView):
    """Вывод авторов"""
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer



# class  AuthorDetaillView(generics.RetrieveAPIView):
#     """Вывод авторов"""
#     queryset = Author.objects.all()
#     serializer_class = AuthorDetailSerializer

