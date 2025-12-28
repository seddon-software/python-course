from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("The index")

def view1(request):
    return HttpResponse(f"This is view1")

def view2(request, param1, param2):
    return HttpResponse(f"view2: param1 = {param1}, param2 = {param2}")

def view3(request):
    return HttpResponse(f"This will use a template")
