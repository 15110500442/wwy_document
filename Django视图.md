# 步骤1：新建一个应用
```python
python manage.py startapp second_app
```
# 步骤2：启动服务器（可选）
```python
python manage.py runserver
```
# 步骤3：在项目的urls.py文件里面添加包含文件
```python
url(r'^second/',include('second.urls'))
```
**注意** 
```text
second后面的的反斜杠千万不要漏掉
```
# 步骤4：在新应用的urls.py里面引入项目的url
**urls.py**
```python
from django.conf.urls import url
from second import views

urlpatterns = [

    url(r'index', views.index),
    url(r'(\d+)/', views.detail),
]
```
**views.py**
```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')


def detail(request, num):
    return HttpResponse(num)
```
# 步骤5：在浏览器输入网址
```python
http://127.0.0.1:8000/second/index
```
# 步骤6：在views.py里面添加
```python
def detail_two(request, num1, num2, num3):
    return HttpResponse('%s-%s-%s' % (num1, num2, num3))
```
# 步骤7：在urls.py里面添加
```python
    # 把之前url注释了
    # url(r'^index', views.index),
    # url(r'^(\d+)/', views.detail),
    url(r'^(\d+)/(\d+)/(\d+)$', views.detail_two),
```
# 步骤8：在urls.py里面添加
```python
# 把其他url注释
url(r'^(?P<num2>\d+)/(?P<num1>\d+)/(?P<num3>\d+)$', views.detail_two),
```