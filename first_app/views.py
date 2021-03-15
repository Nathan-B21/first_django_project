from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.

def root(request):
    return redirect("/blogs")

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

# def index(request):
#     return HttpResponse("placeholder to later display a list of all blogs")
    
def new(request):
    return HttpResponse("Place holder to later display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"place holder to edit blog {number}")

def destory(request, number):
    return redirect("/blogs")

def json(request):
    content = {
        'title' : 'My first blog',
        'content' : 'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'
    }
    return JsonResponse(content)