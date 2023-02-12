
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView


# Create your views here.

class DirectorsListView(ListView):
    template_name = 'kreker/all_directors.html'
    model = Director
    context_object_name = 'directors'

class ActorListView(ListView):
    template_name = 'kreker/all_actors.html'
    model = Actor
    context_object_name = 'actors'

class ActorDetailView(DetailView):
    template_name = 'kreker/one_actor.html'
    model = Actor
    # context_object_name = 'actor'

class DirectorDetailView(DetailView):
    template_name = 'kreker/one_director.html'
    model = Director


def show_all_movie(request):
    movies = Movie.objects.order_by('-name')
    # for movie in movies:
    #     movie.save()
    return render(request, 'kreker/all_movies.html', {
        'movies': movies
    })


def show_one_movie(request ,slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'kreker/one_movie.html', {
        'movie': movie
    })


def all_directors(request):
    directors = Director.objects.all()
    return render(request, 'kreker/all_directors.html', {
        'directors': directors
    })

def one_director(request, id_director):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'kreker/one_director.html', {
        'director': director
    })

def all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'kreker/all_actors.html', {
        'actors': actors
    })

def one_actor(request, id_actor):
    actor = Actor.objects.get(id=id_actor)
    return render(request, 'kreker/one_actor.html', {
        'actor': actor
    })










