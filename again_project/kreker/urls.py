from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all_movie),
    path('movie/<slug:slug_movie>', show_one_movie, name='one_movie'),
    path('directors/', DirectorsListView.as_view(), name='all_directors'),
    path('directors/<int:pk>', DirectorDetailView.as_view(), name='one_director'),
    path('actors/<int:pk>', ActorDetailView.as_view(), name='one_actor'),
    path('actors/', ActorListView.as_view(), name='all_actors'),
]
