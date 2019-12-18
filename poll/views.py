from django.http import HttpResponse

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the resules of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on quesion %s." % question_id)

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")