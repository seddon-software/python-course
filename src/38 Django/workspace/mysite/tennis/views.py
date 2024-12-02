from django.http import HttpResponse
from django.shortcuts import render
from .models import Match
from .forms import InputForm

def index(request):
    return HttpResponse("Tennis index")

# Create your views here.
def homeView(request):
    context = {}
    context['form']= InputForm()
    return render(request, "home.html", context)

# Create your views here.
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
    if request.method == 'POST': # If the form has been submitted...
        form = InputForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            first = request.POST.get('first_name', 'default')
            last = request.POST.get('last_name', 'default')
            # print(form.cleaned_data['my_form_field_name'])
            pass
            
        return HttpResponse(f'{first}/thanks/')
    else:
        form = ContactForm() # An unbound form
    return render_to_response('contact.html', {
        'form': form,
    })

def processForm(request):
    from django import forms
    class NameForm(forms.Form):
        your_name = forms.CharField(label="Your name", max_length=100)
    
    return HttpResponse(f"processForm {request.path}")
    
def f3(request):
    context = {'name':'Chris', 'color':'blue', 'text': 'this is text from the context'}
    return render(request, "tennis/file3.html", context)
