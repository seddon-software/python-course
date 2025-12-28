from django.shortcuts import render

# Create your views here.
from models_app.models import Match


def resultsView(request):
    matches = []
    try:
        for match in Match.objects.all():
            matches.append(match)
    except:
        raise Http404("Problems!!")
    
    context = {
        'matches':matches, 
    }
    return render(request, "resultsTemplate.html", context)
