from django.http import HttpResponse

#투표 상세 화면 출력
def detail(request, question_id): #특별한 결과 없이 값만 출력
    return HttpResponse("You're looking at question %s." % question_id)

#투표 결과 화면 출력
def results(request, question_id):  #특별한 결과 없이 값만 출력
    response = "You're looking at the resules of question %s."
    return HttpResponse(response % question_id)

#투표 기능 화면 출력
def vote(request, question_id): #특별한 결과 없이 값만 출력
    return HttpResponse("You're voting on quesion %s." % question_id)

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")