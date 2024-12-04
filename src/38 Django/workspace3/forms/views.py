from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def homeView(request):
    context = {}
    context['form']= InputForm()
    return render(request, "home.html", context)

def printResults(request):
    context = {
        'first_name':  request.POST.get('first_name'), 
        'last_name':   request.POST.get('last_name'),
        'city':        request.POST.get('city'),
        'country':     request.POST.get('country'),
        'roll_number': request.POST.get('roll_number'),
    }
    return render(request, "mytemplate.html", context)
