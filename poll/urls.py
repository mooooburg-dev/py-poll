from django.urls import path
from . import views

# 네임스페이스 설정
# urls.py에 [app_name]이라는 변수를 추가하고 이름을 설정하면 네임스페이스 설정은 완료.
# 이 네임스페이스를 사용하기 위해서 템플릿에도 수정을 해야함.
app_name = 'poll'

urlpatterns = [
    #poll/views.py가 작동하도록 아래에 URL을 연결

    # ex: /poll/
    path('', views.index, name='index'),

    # ex: /poll/5/
    path('<int:question_id>/', views.detail, name='detail'),    #<>(화살괄호)는 변수를 의미

    # ex: /poll/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /poll/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]