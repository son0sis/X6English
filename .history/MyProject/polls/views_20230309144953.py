from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    myname="Phi Hoan"
    context = {name:myname}
    return render(request, "polls/index.html",context)
