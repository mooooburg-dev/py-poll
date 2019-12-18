from django.urls import path
from . import views

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