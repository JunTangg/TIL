from django.db import models
from django.conf import settings
# Create your models here.
# settings.AUTH_USER_MODEL


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 폭포수(CASCADE) 모델을 적용한다. 하위 요소가 상위 요소에 종속
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
