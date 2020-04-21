from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)  # 짧은 문자열
    pub_date = models.DateTimeField('date published')  # 날짜 필드
    body = models.TextField()  # 긴 문자열

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
