from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def listing(request):
    return HttpResponse("<h1> Listing </h1>")

def profile(request):
    return HttpResponse("<h1> User Profile </h1>")
