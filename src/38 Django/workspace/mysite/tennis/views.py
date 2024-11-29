from django.http import HttpResponse
from django.shortcuts import render
from .models import Match

def index(request):
    return HttpResponse("Tennis index")
    
def filter(request, team):
    hi = request.GET.get('hi', 'default')
    lo = request.GET.get('lo', 'default')
    return HttpResponse(f"Team {team}<br>hi={hi}<br>lo={lo}")

def results(request, team):
    response = f"You're looking at the results for team: {team}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def f1(request, param1, param2):
    return HttpResponse(f"f1 {param1} {param2}")

def f2(request):
    return HttpResponse(f"f2 {request.path}")
    
def f3(request):
    context = {'color':'blue', 'text': 'this is text from the context'}
    return render(request, "tennis/file3.html", context)
