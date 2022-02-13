from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    image = models.ImageField(verbose_name='Изображение автора', upload_to='author_image', blank=True, null=True)
    birthday_year = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name}| {self.last_name}'


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author, verbose_name='Автор')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    image = models.ImageField(verbose_name='Обложка книги', upload_to='book_image', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    release_date = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.name}'
