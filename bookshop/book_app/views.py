from django.shortcuts import render
from .models import *
# Create your views here.

def all_book(request):
    books = Book.objects.all()
    return render(request, 'book_app/all_book.html', {
        'books': books
    })

def one_book(request, id_book):
    book = Book.objects.get(id=id_book)
    return render(request, 'book_app/one_book.html', {
        'book': book
    })