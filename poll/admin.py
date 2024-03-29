#관리자 페이지의 디자인을 변경하고 싶다면,
#django/contrib/admin/templates의 템플릿을 복사해 프로젝트로 가져와 수정할 수 있음

from typing import Any

from django.contrib import admin
from .models import Question, Choice

# 관리자 화면을 커스터마이징 하기 위해서는 admin.py에서 Model Admin을 상속받는 클래스를 만들고 register에 두 번째 인자로 전달해야 한다.

# 답변 항목도 같이 등록 및 수정할 수 있도록 코드 추가(상단에 Choice 모델도 임포트)
# [StackedInline 또는 TabularInline] 클래스를 상속 받음. 그리고 이 클래스를 [QuestionAdmin] 클래스의 아래 [inlines] 클래스 변수에 추가함
#선택하는 방식 - 1.StackedInline
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# 선택하는 방식 - 2.TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets 변수를 이용해 입력/수정 화면에서 각 항목들을 그룹화 하고 그룹의 이름까지 설정할 수 있음.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]

    # 목록에 보이는 항목을 변경할때 list_display 클래스 변수를 추가함.
    # 변수의 값은 튜플로 출력하고 싶은 항목을 묶어서 설정.
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Stacked 또는 Tabular Inline을 상속받은 ChoiceInline 클래스를 inlines 변수에 추가
    inlines = [ChoiceInline]

    # 검색 및 필터 기능 추가
    # list_filter, search_field 클래스 변수를 추가하여 사용할 수 있음
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)