from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


from booksapp.models import Book
from booksapp.serializers import BooksModelSerializer
from booksapp.filters import BookFilter
# from booksapp.serializers import (
#     BooksListSerializer,
#     BooksDetailSerializer,
#     BooksCreateSerializer,
#     BooksUpdateSerializer,
#     BooksDeleteSerializer,
#     AuthorListSerializer,
#     AuthorDetailSerializer,
#     GenreListSerializer,
#     GenreDetailSerializer,
# )



class BooksModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksModelSerializer
    filterset_class = BookFilter
    filter_backends = (DjangoFilterBackend,)



# class BooksListView(generics.ListAPIView):
#     """Вывод списка книг"""
#     queryset = Book.objects.all()
#     serializer_class = BooksListSerializer
#
#
# class BooksDetailView(generics.RetrieveAPIView):
#     """Вывод полного списка книг с описанием, авторами и жанрами"""
#     queryset = Book.objects.all()
#     serializer_class = BooksDetailSerializer
#
#
#
#
# class BooksCreateView(generics.CreateAPIView):
#     """Создание книг"""
#     queryset = Book.objects.all()
#     serializer_class = BooksCreateSerializer
#
#
# class BooksUpdateView(generics.RetrieveUpdateAPIView):
#     """Редактирование созданной книг"""
#     queryset = Book.objects.all()
#     serializer_class = BooksUpdateSerializer
#
#
# class BooksDeleteView(generics.RetrieveDestroyAPIView):
#     """Удаление созданной книг"""
#     queryset = Book.objects.all()
#     serializer_class = BooksDeleteSerializer
#
#
# class AuthorListView(generics.ListAPIView):
#     """Вывод авторов"""
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer
#
#
# class AuthorDetailView(generics.RetrieveAPIView):
#     """Вывод авторов"""
#     queryset = Author.objects.all()
#     serializer_class = AuthorDetailSerializer
#
#
# class GenreListView(generics.ListAPIView):
#     """Вывод авторов"""
#     queryset = Genre.objects.all()
#     serializer_class = GenreListSerializer
#
#
# class GenreDetailView(generics.RetrieveAPIView):
#     """Вывод авторов"""
#     queryset = Genre.objects.all()
#     serializer_class = GenreDetailSerializer
