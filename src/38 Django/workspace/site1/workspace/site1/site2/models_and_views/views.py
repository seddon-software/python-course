from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the models_and_views app index.")
