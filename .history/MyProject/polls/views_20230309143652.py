from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')
def ham1(request):
    return HttpResponse("<h1>Hello</h1>")