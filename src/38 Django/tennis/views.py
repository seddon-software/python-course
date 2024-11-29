from django.http import HttpResponse
from .models import Match

def index(request):
    from django.shortcuts import render
    context = {}
    return render(request, "file3.html", context)
    
def filter(request, team):
    a = request.GET.get('a', 'default')
    b = request.GET.get('b', 'default')
    return HttpResponse(f"Team {team}{a}{b}")

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
    from django.shortcuts import render
    context = {}
    return render(request, "file3.html", context)
