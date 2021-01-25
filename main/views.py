from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

def homepage(request):
    return render(request, "index.html")
    
def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    book = Book(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["year"][:10]
    )
    book.save()
    return redirect(books)