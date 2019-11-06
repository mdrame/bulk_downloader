from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Home Page </h1>")

def listing(request):
    return HttpResponse("<h1> Listing </h1>")

def profile(request):
    return HttpResponse("<h1> User Profile </h1>")
