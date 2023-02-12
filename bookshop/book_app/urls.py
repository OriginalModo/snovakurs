from django.urls import path, include
from .views import *

urlpatterns = [
    path('', all_book),
    path('book/<int:id_book>', one_book, name='one_book'),
]
