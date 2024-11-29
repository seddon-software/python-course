from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the tennis index.")
    
def detail(request, team):
    return HttpResponse(f"Team {team}")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    
