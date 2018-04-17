# 创建一个项目bcxt_tmpl 
# 创建一个应用learn
# 配置url
* 1. 在应用下创建一个urls.py模块
* 2. 把我们应用创建的urls.py引入到项目里(做好关联)
```python
url(r'^learn/', include(learn.urls))
```
# 视图
* 1. 首先应该先创建HTML页面
```
默认配置下，Django 的模板系统会自动找到app下面的templates文件夹中的模板文件。
```
* 2. 创建视图
```python
def home(request):
    return render(request, 'home.html')
```
* 3. 配置url
```python
from django.conf.urls import url
from learn import views

urlpatterns = [
    url(r'^home/$', views.home)
]
```
* 4. 跑起django项目
```python
python manage.py runserver
```
* 5. 在浏览器输入
```python
http://127.0.0.1:8000/learn/home/
```
* 注意：render 是返回模板渲染

# 模板
## 显示一个基本的字符串在网页上
### 步骤1（思路：在视图里面定义）：
```python
from django.shortcuts import render


# Create your views here.
def home(request):
    string = '欢迎来到北财学堂'
    return render(request, 'home.html', {'string': string})
```
```python
from django.shortcuts import render


# Create your views here.
def home(request):
    string = '欢迎来到北财学堂'
    context = {'string': string}
    return render(request, 'home.html', context)
```
### 步骤2：在HTML里面渲染 {{ }}
* 在home.html里面
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>
<h1>{{ string }}</h1>
</body>
</html>
```
## 基本的 for 循环 和 List内容的显示
> 简单总结一下：一般的变量之类的用 {{ }}（变量），功能类的，比如循环，条件判断是用 {%  %}（标签）
* 1. 在视图函数里面定义一个列表给模板传过去
```python
from django.shortcuts import render


# Create your views here.
def home(request):
    alist = ['python全栈+人工智能', '大数据技术', 'HTML5', 'UI设计']
    context = {'a': alist}
    return render(request, 'home.html', context)
```
* 2. 在模板里面操作
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>
{% for xxxxx in a %}
    <h1>{{ xxxxx }}</h1>
    <hr>
{% endfor %}

</body>
</html>
```
## 显示字典中内容
* 步骤1 在views.py里面配置内容
```python
from django.shortcuts import render


# Create your views here.
def home(request):
    adict = {'one': '蒙多', 'two': '猪妹'}
    context = {'a': adict}
    return render(request, 'home.html', context)

```
* 步骤2：在模板里面获取内容并展示
* 调用字典的值可以用 键名（context）+键名（adict的键)
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>
<h1>one:{{ a.one }}</h1>
<h2>two:{{ a.two }}</h2>
</body>
</html>
```
## 在模板进行 条件判断和 for 循环的详细操作
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>
{% for item in List %}
    {{ item }}{% if not forloop.last %},{% endif %}
{% endfor %}
</body>
</html>
```
```python
from django.shortcuts import render


# Create your views here.
def home(request):
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'home.html', {'List': List})

```
## 网页跳转
* urls.py
```python
from django.conf.urls import url
from learn import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^detail/$', views.detail, name='deat')
]

```
* views.py
```python
def detail(request):
    return render(request, 'detail.html')
```
* 最关键的一步，我们如何在网页中进行跳转,利用模板语法
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>

<a href="{% url 'deat' %}">跳转</a>
</body>
</html>
```
