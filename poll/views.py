from django.http import HttpResponse, Http404
from django.template import loader  #템플릿을 불러오기 위해 loader 임포트
from django.shortcuts import render, get_object_or_404

from .models import Question

#인덱스 화면 출력
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   #질문 리스트 5개만 가져오기

    # 1.render 메서드를 사용하지 않고 아래와 같이 코드 작성 가능
    # template = loader.get_template('polls/index.html')  # .html 템플릿 연결하기
    # context = { #latest_question_list(투표목록) 변수를 전달하기 위한 context
    #     'latest_question_list':latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 2.위 방법이 번거롭게 느껴진다면 render 메서드를 활용해서 아래와 같이 작성 가능
    context = { 'latest_question_list': latest_question_list } # latest_question_list(투표목록) 변수를 전달하기 위한 context
    return render(request, 'polls/index.html', context)

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


#투표 상세 화면 출력
def detail(request, question_id): #특별한 결과 없이 값만 출력
    # 1. 투표 상세 목록을 불러옴. 불러올 항목이 없을 경우 404 에러를 발생시킨다.
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise  Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

    # 2. get_object_or_404 메서드를 활용해 위의 코드를 간소화 시킬 수 있다.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

    # return HttpResponse("You're looking at question %s." % question_id)

#투표 결과 화면 출력
def results(request, question_id):  #특별한 결과 없이 값만 출력
    response = "You're looking at the resules of question %s."
    return HttpResponse(response % question_id)

#투표 기능 화면 출력
def vote(request, question_id): #특별한 결과 없이 값만 출력
    return HttpResponse("You're voting on quesion %s." % question_id)

