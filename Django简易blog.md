#Django基本用法复习+简易blog搭建
## 一、目标
1. 掌握Django的基本用法
2. 了解Django的部分原理以及各组件的含义
3. 可以独立使用Django进行基本的网站开发
## 二、课程内容
1. 了解Django
2. 搭建开发环境
3. 完成一个简单的个人博客网站
## 三、课程知识要求
1. 掌握python语言
2. 了解HTML语言
3. 了解浏览器上网的基本原理
## 四、课前准备
> **知道什么是Django?**
1. Django是一个基于Python的``高级web开发框架``
2. 它能够让开发人员进行``高效``且``快速``的开发
3. 高度集成(不用自己造轮子),并且免费开源
## 五、知识补充
> 正常上网流程
 1. 打开浏览器--->地址栏输入网址--->敲下回车（向**目标URL发送了一个``HTTP请求``**--->服务器把页面响应给浏览器）--->看到网页

> 浏览器浏览网页的基本原理
1. 本质是``网络通信``,即通过网络进行数据传递
2. 浏览器经过通信后获取到该页面的源代码文档（HTML等）
3. 浏览器解析文档以后以适当的形式展现给用户

![22](https://i.loli.net/2018/04/17/5ad5e8aa4aa65.png)
 
## 六、搭建环境
> Linux(Ubuntu发行版)
1. Python(python3.5.2+)
2. Virtualenv和Virtualenvwrapper
3. Django(1.8.2)
4. Pymysql
## 七、开发工具
> 编辑器推荐
1. PyCharm
2. VSCode
3. Sublime Text3,Atom
4. Vim,Emacs
* 注意：怎么爽怎么来，爱用啥编辑器都行，但是PyCharm功能比较强大，其他编辑器需要通过安装插件来实现相关功能
## 八、创建项目和应用
###步骤：
1. 创建虚拟环境并配置相关环境（命令行）
```
# 创建虚拟环境
1. mkvirtualenv myblog_env
# 进入（使用）虚拟环境
2. workon myblog_env
# 配置项目一些基础环境(可以使用豆瓣源进行加速)
# Django框架
3. pip install django==1.8.2 -i https:pypi:douban.com/simple
# python-mysql驱动
4. pip install pymysql -i https:pypi:douban.com/simple
# 在命令行写测试代码的时候用（可选）
5. pip install ipython -i https:pypi:douban.com/simple
```
2. 创建项目
```python
django-admin startproject myblog
```
> 注释：
> **1**. manage.py ---与项目进行交互的命令行工具集的入口  
> **2**. myblog目录  ---项目的一个容器，包含项目最基本的一些配置，目录名称``不建议修改``
> **2**. wsgi.py ---Python服务器网关接口(Python应用与web服务器之间的接口)，``是整个Django项目的关键``
> **3**. urls.py ---URL配置文件，Django项目中所有地址（页面）都需要我们自己去配置其URL
> **4**. settings.py --是配置文件，是整个项目最核心最重要的配置文件，里面包含了数据库、web应用、时间等各种配置
> **5**. Template ---Django模板
> **6**. _ _init_ _.py ---Python中声名包

3. 创建应用(进入项目目录下)
###步骤：
1. 打开命令行，进入项目中manage.py同级目录后输入：
```python
python manage.py startapp blog
```
2. 添加应用名到settings.py的INSTALLED_APPS列表里面，注意，应用名不可以和python模块同名，譬如os等等...
> 注释:
> 1. migrations ---数据移植（迁移）模块
> 2. admin ---当前应用的后台管理系统，这是Dajngo的一大特点，每个应用都有自带的admin后台管理系统
> 3. models.py 数据模型模块（使用ORM框架）类似MVC（MVT）中的models
> 4. views.py 执行响应的代码所在模块，代码逻辑处理的主要地点，项目中大部分的代码都在这里编写

## 九、创建一个（简单）响应（HttpResponse对象)
###步骤：
1. blog应用下的views.py导入
```python
from django.http import HttpResponse
```
2. 编写一个简单的视图函数
```python
def index(request):
    return HttpResponse('hello,world')
```
* 注意
> 1. 每个响应对应一个函数，函数必须返回一个响应
> 2. 函数必须存在一个参数，一般约定为request
> 3. 每一个响应（函数）对应一个url
3. 配置url
* 创建一个应用的urls.py文件
* 在myblog项目里面引用应用的urls.py文件并进行相应的配置
```python
from django.conf.urls import include, url
from django.contrib import admin
from blog import urls as blog_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls))
]
```
4. 配置应用下面的urls.py模块
```python
from django.conf.urls import include

urlpatterns = [
   
]
```
5. 导入视图模块，编写url
```python
from django.conf.urls import url
from blog import views as blog_views

urlpatterns = [
    url(r'^index/$', blog_views.index)
]
```
* 注意
> **1**. 每一个URL都以url()的形式写出来
> **2**. url函数放在urlpatterns列表里面
> **3**. url函数有三个参数:URL(正则),对应方法，名称
> **4**. 用正则表达式来约束我们的url
6. 启动服务
```
python manage.py runserver
```
## 十、Templates
###HTML文件：
> 1. 使用了Django模板语言引擎（Django Template Language,DTL)
> 2. 也可以使用第三方的模板语言引擎 Jinja2
###步骤：
1. 在template目录下创建HTML文件（暂时取名index）
2. 在views.py下返回一个render()
```python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')
```
> DTL基本使用:
1. ``render()``函数中支持一个``dict类型``的参数,该字典是后台传递到模板的参数，``键为参数名``
2. 在模板中使用``{{参数名}}``来直接使用
例如：views.py下:
```python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html', {'hello': 'hello ,Blog'})

```
index.html接收：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{ hello }}</h1>
</body>
</html>
```
## 十一、Model
> Django中的models是什么？
1. 通常，``一个Model``对应数据库的一张数据表
2. Django中Model以``类``的形式表现
3. 它包含了一些``基本字段``以及数据的``一些行为``
> ORM
1. ``对象关系映射``（Object Relation Mapping）
2. 实现了``对象和数据库``之间的映射
3. 隐藏了数据访问的细节,不需要编写SQL语句
### 步骤:
* 1.创建类,继承``models.Model``,该类即是一张数据表,在类里面去创建数据表的字段
* 2.创建字段,字段即是类里面的``属性``（变量）
**语法结构：attr = models.CharField(max_length=64)**
>在models.py中:
```python
from django.db import models


# Create your models here.
class Article(models.Model):
    # max_length为CharFiled必填选项   default可选
    title = models.CharField(max_length=30, default='Title')
    # null=True 表示允许为空
    content = models.TextField(null=True)
```
* 3.命令行进入manage.py同级目录,执行``python manage.py makemigrations app名（app名可选）``生成数据迁移
* 4.（执行）迁移``Python manage.py migrate``
## 十二、呈现页面数据
* 后台：views.py中import models
```python
from django.shortcuts import render
from django.http import HttpResponse
from blog import models


# Create your views here.
def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'index.html', {'art': article})
```
* 前端：模板可以直接使用对象以及对象的"."操作：``{{art.title}}``
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{ art.title }}</h1>
<h3>{{ art.content }}</h3>
</body>
</html>
```
## 十三、Admin(Django——Admin很强大)
> 什么是Admin?
* Admin是Django自带的一个功能强大的``自动化数据管理界面``被授权的用户可以直接在Admin中``管理数据库``
* Django提供很多针对Admin的``定制功能``
### 配置Admin
1. 创建用户
```python 
# 创建超级用户
python manage.py createsuperuser 
# 之后输入用户名和邮箱
```
2. 入口: 路径+端口号/admin/Admin
3. 设置成中文：settings.py中的LANGUAGE_CODE='zh_Hans'
4. 要操作数据需要先配置应用:
* 在应用下面admin.py中引入自身models模块(或里面的模型类),然后编写:
```python 
from django.contrib import admin
from blog import models

# Register your models here.

admin.site.register(models.Article)
```
### 定制Admin
#### 修改数据默认显示名称
##### 步骤：
1. 在Article类下添加一个方法
2. 根据Python版本选择__str__(self)或__unicode__(self) 返回标题即可
* __str__(self) python3
* __unicode__(self) python2
```python
from django.db import models


# Create your models here.
class Article(models.Model):
    # max_length为CharFiled必填选项   default可选
    title = models.CharField(max_length=30, default='Title')
    # null=True 表示允许为空
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
```
![23](https://i.loli.net/2018/04/18/5ad626716e974.png)

## 十四、博客主页面开发
### 页面内容
####一. 博客主页面
####二. 博客文章内容页面
####三. 博客撰写页面

####**一. 博客主页面内容**
#####1.文章标题列表，超链接
**列表编写思路:**
* 取出数据库中所有文章对象
* 将文章对象打包成列表，传递到前端
* 前端页面把文章以标题超链接的形式逐个列出
**views.py中:**
```python
from django.shortcuts import render
from django.http import HttpResponse
from blog import models


# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles_List': articles})

```
**html页面中:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1><a href="#">新文章</a></h1>
{% for article in articles_List %}
    <a href="#">{{ article.title }}</a>
    <br>
{% endfor %}
</body>
</html>
```
#####2.发表博客按钮（超链接）

##十五、博客文章页面
### 页面内容
####一. 标题
####二. 文章内容
####三. 修改文章按钮(超链接)

**views.py中：**
```python
from django.shortcuts import render
from django.http import HttpResponse
from blog import models


# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles_List': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})
```
**创建一个HTML（article_page.html）**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{ article.title }}</h1>
<br>
<h3>{{ article.content }}</h3>
<br>
<br>
<a href="">修改文章</a>
</body>
</html>
```
**urls.py中：**
```python
from django.conf.urls import url
from blog import views as blog_views

urlpatterns = [
    url(r'^index/', blog_views.index),
    url(r'article/(?P<article_id>[0-9]+)$', blog_views.article_page)
]
```
**注意**
1. 参数写在响应函数中request后，可以有默认值
2. URL正则表达式:**r'article/(?P<article_id>[0-9]+)$'**
3. URL正则中的``组名必须和参数名一致``

## Django模板中的超级链接配置
> 超链接目标地址
1. href后面是目标地址
2. template中可以使用：url+命名空间名:链接名+参数
即:
```html
{%url app_name:url_name param %}
```
**其中app_name和url_name都在url中配置**

3. 再配url：
> url函数的名称参数:(主要取决于**是否使用了include引用了另外一个url配置文件**)
* 方案1：根据urls,写在``include()``的第二个参数位置,**namespace='blog'**
* 方案2：应用下则写在``url()``的三个参数的位置,``name='article'``

**根urls.py中:**
```python
from django.conf.urls import include, url
from django.contrib import admin
from blog import urls as blog_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls,namespace='blog'))
]
```
**子urls.py中:**
```python
from django.conf.urls import url
from blog import views as blog_views

urlpatterns = [
    url(r'^index/', blog_views.index),
    url(r'article/(?P<article_id>[0-9]+)$', blog_views.article_page,name='article_page')
]
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1><a href="#">新文章</a></h1>
{% for article in articles_List %}
    <a href="{% url 'blog:article_page' article.id %}">{{ article.title }}</a>
    <br>
{% endfor %}
</body>
</html>
```
## 十六、博客撰写页面
###页面内容
####标题编辑栏
####文章内容编辑区域
####提交按钮
**创建一个编辑页面(edit_page.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>编辑页面</title>
</head>
<body>
<form action="#" method="post">
    文章标题：
    <input type="text" name="title">
    <hr>
    文章内容:
    <input type="text" name="content">
    <input type="submit">
</form>
</body>
</html>
```



