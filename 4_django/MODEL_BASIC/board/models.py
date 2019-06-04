from django.db import models


class Article(models.Model):
    # id = Primary Key
    title = models.CharField(max_length=200)      # CharField: 최대 길이를 반드시 지정해주어야 한다
    content = models.TextField()                  # TextField: 무제한 문자열

    def __str__(self):
        return f'{self.id}: {self.title} - {self.content}'

