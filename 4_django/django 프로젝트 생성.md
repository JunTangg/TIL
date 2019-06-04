# django 프로젝트 생성

장고 확장팩 설치

```sh
pip install django-extensions ipython ipython[notebook]
```

settings.py

```python
INSTALLED_APPS = [
    'django_extensions',   # 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',               # 내가 만들 앱 추가
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

```

## 프로젝트 새로 만들기

1. 프로젝트 만들기

   ```sh
   django-admin startproject model_basic
   ```

2. 앱 만들기

   ```sh
   django-admin startapp board
   ```

3. masterapp urls.py 

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('board/', include('board.urls')),
   ]
   ```

4. 앱 urls.py

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index),
   ]
   ```

5. 앱 views.py

   ```python
   from django.shortcuts import render
   
   
   def index(request):
       return render(request, 'board/index.html')
   ```

6. templates > board 디렉토리 만들기

7. base.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Board</title>
   </head>
   <body>
   {% block body %}
   {% endblock %}
   </body>
   </html>
   ```

8. index.html

   ```html
   {% extends 'board/base.html' %}
   
   {% block body %}
   
   {% endblock %}
   ```

   