from django.urls import path
from . import views

# 네임스페이스 설정
# urls.py에 [app_name]이라는 변수를 추가하고 이름을 설정하면 네임스페이스 설정은 완료.
# 이 네임스페이스를 사용하기 위해서 템플릿에도 수정을 해야함.
app_name = 'poll'


# 클래스형 뷰로 변경한 코드
# 아래 함수형 뷰와 다른 점은,
# route 패턴에 들어있는 패턴이름과 view 인자
# 패턴이름을 question_id에서 pk로 변경했음. 그리고 뷰 이름을 바꾸고 뒤에 추가 코드를 붙임.
# 함수형 뷰를 사용할 떄는 뷰를 그대로 써주면 되지만 클래스형 뷰를 사용할 떄는 꼭 뒤에 [as_view()]를 붙여야 하기 때문임.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



# 함수형 뷰
# urlpatterns = [
#     #poll/views.py가 작동하도록 아래에 URL을 연결
#
#     # ex: /poll/
#     path('', views.index, name='index'),
#
#     # ex: /poll/5/
#     path('<int:question_id>/', views.detail, name='detail'),    #<>(화살괄호)는 변수를 의미
#
#     # ex: /poll/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#
#     # ex: /poll/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]