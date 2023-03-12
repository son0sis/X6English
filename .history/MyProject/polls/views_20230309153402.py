from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    myname="Phi Hoan"
    taisan = ["phone","laptop"]
    context = {"name":myname,"item":taisan}
    return render(request, "polls/index.html",context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"dsquest":list_question}
    return render(request,"polls/question_list.html",context)