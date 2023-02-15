from django.contrib import admin
from .models import *
from django import forms
# Register your models here.


# admin.site.register(Director)
# admin.site.register(Actor)
# admin.site.register(DressingRoom)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'director', 'budget')
    list_editable = ('rating', 'director', 'budget')
    list_per_page = 10
    prepopulated_fields = {'slug':('name',)}
    # filter_horizontal = ('actors',)
    filter_vertical = ('actors',)

# admin.site.register(Movie, MovieAdmin)

@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ('floor', 'number', 'actor')

@admin.register(Director)
class Director(admin.ModelAdmin):
    list_display = ('first_name', 'director_email')

@admin.register(Actor)
class Director(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')