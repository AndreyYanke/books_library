from rest_framework import serializers

from booksapp.models import Book, Author


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

