from rest_framework import serializers

from booksapp.models import Book, Author, Genre


class AuthorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания автора для детального отображения в книге"""

    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class GenreDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания жанра для детального отображения в книге"""

    class Meta:
        model = Genre
        fields = ('name',)


class BooksModelSerializer(serializers.ModelSerializer):
    """Вывод полного описания книги с авторами и жанрами"""
    authors = AuthorDetailSerializer(read_only=True, many=True)
    genre = GenreDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = '__all__'

