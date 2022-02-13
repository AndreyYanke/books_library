from django.urls import path

from . import views

app_name = 'booksapp'


urlpatterns = [
    path('', views.BooksListView.as_view()),
    path('author/', views.AuthorListView.as_view()),
]