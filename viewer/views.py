from logging import getLogger

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

from .forms import MovieForm, GenreForm
from .models import Movie

LOGGER = getLogger()


def about_view(request):
    return render(
        request,
        "about.html"
    )


def index(request):
    return render(request, template_name="base.html")


def test_view(request):
    return render(request, template_name="test.html")


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


# class MovieCreateView(FormView):
#     form_class = MovieForm
#     template_name = "form.html"
#     success_url = reverse_lazy("movies")
#
#     # this is executed when the form is valid
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#         Movie.objects.create(
#             title=cleaned_data['title'],
#             genre=cleaned_data['genre'],
#             rating=cleaned_data['rating'],
#             released=cleaned_data['released'],
#             description=cleaned_data['description'])
#         return result
#
#
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data in the movie creation form', )
#         messages.error(self.request, "Invalid data provided", extra_tags="warning")
#         return super().form_invalid(form)

class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = "customized_form.html"
    success_url = reverse_lazy('movies')
    form_class = MovieForm

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data in the movie creation form.', )
        messages.error(self.request,
                       "Invalid data provided",
                       extra_tags="btn-warning")
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'customized_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')


class GenreCreateView(LoginRequiredMixin, CreateView):
    template_name = "form.html"
    success_url = reverse_lazy('movies')
    form_class = GenreForm


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Movie
    success_url = reverse_lazy('movies')


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


