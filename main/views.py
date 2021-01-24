from django.shortcuts import render, HttpResponse, test
from .models import ToDo, Book

def homepage(request):
    return render(request, "index.html")
    
def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


#def third(request):
    #return HttpResponse("This is page test3")

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})