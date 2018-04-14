## 步骤1：新建一个应用
```python
python manage.py startapp second_app
```
## 步骤2：启动服务器（可选）
```python
python manage.py runserver
```
## 步骤3：在项目的urls.py文件里面添加包含文件
```python
url(r'^second/',include('second.urls'))
```

**注意** 
```text
second后面的的反斜杠千万不要漏掉
```
## 步骤4：配置应用url
**urls.py**
```python
from django.conf.urls import url
from second import views

urlpatterns = [

    url(r'^index/', views.index),
    url(r'^(\d+)/', views.detail),
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
## 步骤5：在浏览器输入网址
```python
http://127.0.0.1:8000/second/index
```
## 步骤6：在views.py里面添加
```python
def detail_two(request, num1, num2, num3):
    return HttpResponse('%s-%s-%s' % (num1, num2, num3))
```
## 步骤7：在urls.py里面添加
```python
    # 把之前url注释了
    # url(r'^index', views.index),
    # url(r'^(\d+)/', views.detail),
    url(r'^(\d+)/(\d+)/(\d+)$', views.detail_two),
```
## 步骤8：在urls.py里面添加
```python
# 把其他url注释
url(r'^(?P<num2>\d+)/(?P<num1>\d+)/(?P<num3>\d+)$', views.detail_two),
```
# 定义视图
## 1.在项目settings里面,把debug改为Ture
```python
DEBUG=False
```
## 2.在项目settings里面，把ALLOWED_HOSTS改为任何人可以访问
```python 
ALLOWED_HOSTS=['*']
```
## 3.在项目的templates目录下面添加404.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>傻了吧,找不到页面</h1>
</body>
</html>
```
# HttpReqeust对象
## 1.在应用的urls.py里面设置重新配置一下url
```python
urlpatterns = [
    url(r'^index', views.index),
]
```
## 2.修改应用views.py的视图函数
```python
def index(request):
    # request返回请求页面的完整路径
    return HttpResponse(request.path)
```
## 3.将应用跑起来，然后再浏览器输入如下路径,注意：此时页面显示的为路径
```chrome
http://127.0.0.1:8000/second/index
```
# GET属性

## 1.在应用templates里面创建一个目录，目录名为templates,添加3个html页面,分别为getTest1.html,getTest2.html,getTest3.html
## 2.在应用的views.py里面的增加3个视图函数
```python
# 展示接收的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')
# 接收一键一值的情况
def getTest2(request):
    return render(request,'booktest/getTest2.html')
# 接收一键多值的情况
def getTest3(request):
    return render(request,'booktest/getTest3.html')
```
## 3.在应用的urls.py里面添加
```python
    url(r'^index', views.index),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
```
## 4.在getTest1.html
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
一键一值：<a href="/second/booktest/getTest2/?a=1&b=2&c=3">test2</a>
<hr>
一键多值：<a href="/second/booktest/getTest3/?a=1&b=2&c=3">test3</a>
</body>
</html>
```

## 5.在views.py
```python
# 展示接收的页面
def getTest1(request):
    return render(request, 'booktest/getTest1.html')


# 接收一键一值的情况
def getTest2(request):
    # request.GET['a']等价于request.GET.get('a')
    # 根据键接收值
    a1 = request.GET.get('a')
    b1 = request.GET.get('b')
    c1 = request.GET.get('c')
    # 构造上下文
    context = {'a': a1, 'b': b1, 'c': c1}
    # 调用模板进行渲染
    return render(request, 'booktest/getTest2.html', context)


# 接收一键多值的情况
def getTest3(request):
    return render(request, 'booktest/getTest3.html')
```
## 6.在getTest2.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
a:{{ a }}
<hr>
b: {{ b }}
<hr>
c:{{ c }}
<hr>
</body>
</html>
```
## 7.接收一键多值,在views.py模块里面
* 在浏览器输入 http://127.0.0.1:8000/second/getTest3/?a=12&a=2&a=3 (其中a对应多个值)
```python
def getTest3(request):
    a1 = request.getlist('a')
    context={'a':a1}
    return render(request, 'booktest/getTest3.html',context)
```
## 8.在getTest3.html里面
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>页面3</title>
</head>
<body>
a:{% for item in a %}
{{ item }}
{% endfor %}
</body>
</html>
```
# POST请求
## 设计2个视图
```python
def postTest1(request):
    return render(request, 'booktest/postTest1.html')


def postTest2(request):
    return render(request, 'booktest/postTest2.html')
```
## 配置url(urls.py)
```python
urlpatterns = [
    url(r'^index/', views.index),
    # url(r'^(\d+)/',views.detail)
    url(r'(?P<num2>\d+)/(?P<num1>\d+)/(?P<num3>\d+)', views.detail2),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$',views.postTest2),
]
```
## 添加html模板
1. postTest1.html
```html
{# action 为要请求的url#}
<form method="post" action="/second/postTest1">
    用户名：<input type="text" name="uname">
    <hr>
    密码：<input type="password" name="upwd">
    <hr>
    性别:<input type="radio" name="ugender" value="男" checked="checked">男<input type="radio" name="ugender" value="女">女
    <hr>
    <input type="submit" value="提交">
```
2. postTest2.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>POST2</title>
</head>
<body>
{# action 为要请求的url#}
<form method="post" action="/second/postTest2"></form>
</body>
</html>
```