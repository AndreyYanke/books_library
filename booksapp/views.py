from rest_framework import generics

from booksapp.models import Book, Author, Genre
from booksapp.serializers import (
    BooksListSerializer,
    BooksDetailSerializer,
    BooksCreateSerializer,
    BooksUpdateSerializer,
    AuthorListSerializer,
    AuthorDetailSerializer,
    GenreListSerializer,
    GenreDetailSerializer,
)


class BooksListView(generics.ListAPIView):
    """Вывод списка книг"""
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer


class BooksDetailView(generics.RetrieveAPIView):
    """Вывод полного списка книг с описанием, авторами и жанрами"""
    queryset = Book.objects.all()
    serializer_class = BooksDetailSerializer


class BooksCreateView(generics.CreateAPIView):
    """Создание книг"""
    queryset = Book.objects.all()
    serializer_class = BooksCreateSerializer

class BooksUpdateView(generics.UpdateAPIView):
    """Редактирование созданной книг"""
    queryset = Book.objects.all()
    serializer_class = BooksUpdateSerializer


class AuthorListView(generics.ListAPIView):
    """Вывод авторов"""
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    """Вывод авторов"""
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer


class GenreListView(generics.ListAPIView):
    """Вывод авторов"""
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer


class GenreDetailView(generics.RetrieveAPIView):
    """Вывод авторов"""
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer
