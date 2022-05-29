from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from viewer.views import (
    about_view, index, test_view,
    MoviesView, MovieCreateView, GenreCreateView, MovieUpdateView, MovieDeleteView, MovieDetailView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path("", index, name="index"),
    path("test/", test_view, name="test"),
    path("movies/", MoviesView.as_view(), name="movies"),
    path("add_movies/", MovieCreateView.as_view(), name="add_movie"),
    path("add_genre/", GenreCreateView.as_view(), name="add_genre"),
    path("update_movie/<pk>", MovieUpdateView.as_view(), name="update_movie"),
    path("delete_movie/<pk>", MovieDeleteView.as_view(), name="delete_movie"),
    path("movie_detail/<pk>", MovieDetailView.as_view(), name="movie_detail"),
    path('accounts/', include('accounts.urls', namespace='accounts'))
]
