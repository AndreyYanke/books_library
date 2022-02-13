from django.urls import path

from . import views

app_name = 'booksapp'


urlpatterns = [
    path('', views.BooksListView.as_view()),
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorDetailView.as_view()),
    path('genre/', views.GenreListView.as_view()),
    path('genre/<int:pk>/', views.GenreDetailView.as_view()),
]