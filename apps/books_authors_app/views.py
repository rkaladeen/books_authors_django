from django.shortcuts import render, redirect
from .models import *

def index(request):
  context = {
    "all_books" : Book.objects.all()
  }
  return render(request, "books_authors_app/index.html", context)

def add_book(request):
  Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
  return redirect("/")

def authors(request):
  context = {
    "all_authors" : Author.objects.all()
  }
  return render(request, "books_authors_app/author.html", context)

def add_author(request):
  Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['note'])
  return redirect("/authors")

# Book Information
def book_info(request, bkid):
  book_id = Book.objects.get(id=bkid)
  
  context = {
    "book" : book_id,
    "book_authors" : book_id.authors.all(),
    "other_authors" : Author.objects.all() # Need to figure out how to exclude to show only remaining authors in dropdown menu
  }
  return render(request, "books_authors_app/book-info.html", context)

def add_author_to_book(request, bkid):
  book_id = Book.objects.get(id=bkid)
  new_author = request.POST['add-author']
  book_id.authors.add(Author.objects.get(id=new_author))
  return redirect(f"/books/{bkid}")

# Author Information
def author_info(request, atid):
  author_id = Author.objects.get(id=atid)

  context = {
    "author" : author_id,
    "books" : author_id.books.all(),
    "other_books" : Book.objects.all()
  }
  return render(request, "books_authors_app/author-info.html", context)

def add_book_to_author(request, atid):
  author_id = Author.objects.get(id=atid)
  new_book = request.POST['add-book']
  author_id.books.add(Book.objects.get(id=new_book))
  return redirect(f"/authors/{atid}")