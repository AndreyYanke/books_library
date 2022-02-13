from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from booksapp.filters import BookFilter
from booksapp.models import Book
from booksapp.serializers import BooksModelSerializer


class BooksModelViewSet(ModelViewSet):
    queryset = Book.objects.prefetch_related('authors').all()
    serializer_class = BooksModelSerializer

    filter_backends = (DjangoFilterBackend,)
    renderer_classes = (TemplateHTMLRenderer,)

    def list(self, request, *args, **kwargs):
        self.queryset = self.filter_queryset(self.get_queryset())
        context = {'filter': BookFilter(self.request.GET, queryset=self.get_queryset())}
        return Response(context, template_name='booksapp/books.html')
