from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello word!")
def ham1(request):
    return HttpResponse("<h1>Hello</h1>")