from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Film
# Create your views here.

class FilmBaseView(View):
    model = Film
    fields ='__all__'
    success_url = reverse_lazy('films:all')

class FilmListView(FilmBaseView, ListView):
    ...

class FilmDetailView(FilmBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class FilmCreateView(FilmBaseView, CreateView):
    """View to create a new film"""

class FilmUpdateView(FilmBaseView, UpdateView):
    """View to update a film"""

class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film"""
    