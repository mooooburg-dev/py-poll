import datetime

from django.db import models
from django.utils import timezone
#

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date' # 원칙적으로 임의의 메서드에 의한 값은 정렬이 불가능함. 대신 다른 값을 기준으로 정렬할 수 있는데 이 기준 항목을 설정하는 항목
    was_published_recently.boolean = True # 값이 불리언 값 형태인지 설정. True 설정하면 값 대신 아이콘이 나타남.
    was_published_recently.short_description = 'Published recently?' # 항목의 헤더 이름 설정.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
