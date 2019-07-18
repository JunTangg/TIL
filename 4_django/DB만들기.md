# DB만들기

* Object Relation Mapper
* 파이썬과 SQL 사이의 번역기
* django에서 DB를 다룰 때 필요

models.py

1. 어떤 DB를 만들지 결정

   ```python
   from django.db import models
   
   
   class Article(models.Model):
       title = models.CharField(max_length=200)      # CharField: 최대 길이를 반드시 지정해주어야 한다
       content = models.TextField()                  # TextField: 무제한 문자열
   ```

2. 확인

   ```sh
   python manage.py makemigrations board
   ```

3. migrations > 0001_initial.py 확인

4. DB 생성

   ```sh
   python manage.py migrate board
   ```

5. sqlite 에서 DB파일 확인

6. python manage.py shell

   ```python
   from board.models import Aricle
   article = Article()
   article.title = 'Hi'
   article.content = 'Hello World!'
   article.save()
   # 다른 행을 추가하려면 객체를 새로 만들어야함
   article2 = Article()
   ```



1. ```
   python manage.py shell_plus
   ```

2. ```
   python manage.py shell_plus --notebook
   ```

3. 









