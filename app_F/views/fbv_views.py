from django.shortcuts import render, redirect, get_object_or_404
from ..models import Book
from app_F.models import Book


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'message': 'This is FBVs'
    }
    return render(request, 'books/book_list.html', context)