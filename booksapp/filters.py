from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError

from booksapp.models import Book, Genre


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(method='get_author', label='Автор')
    genre = filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all())
    release_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ('author', 'genre', 'release_date')

    def get_author(self, queryset, name, data):
        try:
            author = data.split()
            return queryset.filter(Q(authors__first_name__iexact=author[0]) | Q(authors__last_name__iexact=author[1]))
        except IndexError:
            raise ValidationError({"error": 'Прошу ввести полное имя и фамилию автора'})








