from rest_framework import serializers

from booksapp.models import Book, Author, Genre


class BooksListSerializer(serializers.ModelSerializer):
    """Вывод списка книг"""

    class Meta:
        model = Book
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    """Вывода автора"""

    class Meta:
        model = Author
        fields = '__all__'


class AuthorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания автора для детального отображения в книге"""

    class Meta:
        model = Author
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):
    """Вывода жанров"""

    class Meta:
        model = Genre
        fields = '__all__'


class GenreDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания жанра для детального отображения в книге"""

    class Meta:
        model = Genre
        fields = '__all__'


class BooksDetailSerializer(serializers.ModelSerializer):
    authors = AuthorDetailSerializer(read_only=True, many=True)
    genre = GenreDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BooksCreateSerializer(serializers.ModelSerializer):
    """Создание книг"""

    class Meta:
        model = Book
        fields = '__all__'


class BooksUpdateSerializer(serializers.ModelSerializer):
    """Редактирование созданной книги"""

    class Meta:
        model = Book
        fields = '__all__'
