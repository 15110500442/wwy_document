# 模型
## 1、判断（判等）  exact
* 查询编号为1的图书
```python
BookInfo.book.filter(id=1)
BookInfo.book.filter(id__exact=1)
注意：exact可以省略
```
## 2、模糊查询
* 查询书名包含"传"的图书 contains
```python
BookInfo.book.filter(btitle__contains='传')
```
* 查询书名以"射"开头
```python
 BookInfo.book.filter(btitle__startswith='射')
```
* 查询书名以狐结尾的
```python
BookInfo.book.filter(btitle__endswith='狐') 
```
## 3、空值查询 isnull
* 查询书名不为空的图书
```python
BookInfo.book.filter(btitle__isnull=False)
```
## 4、范围查询 where id in (1,3,5)
* 查询编号为1或3或者5的图书
```python
BookInfo.book.filter(id__in=[1,3,5])
```
## 5、比较查询 gt lt(less than) gte lte
* 查询编号大于等于3的图书
```python
BookInfo.book.filter(id__gte=3)
```
## 6、日期查询
* 查询1980年发表的书
```python
BookInfo.book.filter(bpub_date__year=1980).values()
```
* 查询1980年1月1日后发表的图书有几本书
```python
BookInfo.book.filter(bpub_date__gt = date(1980,1,1)).count()
```
## 7、exclude:返回不满足条件的数据  --->filter取反
* 查询所有id不为3的图书有多少本
```python
BookInfo.book.exclude(id=3).count()
```
## 8、F对象
* 查询图书阅读量大于评论量的图书信息
```python
BookInfo.book.filter(bread__gt = F('bcomment'))
```
* 查询图书阅读量大于2倍的评论量的图书信息
```python
BookInfo.book.filter(bread__gt = F('bcomment')*2)
```
## 9、Q对象
* 查询id大于3``且``阅读量大于30的图书信息
```python
# 方案1
BookInfo.book.filter(id__gt=3,bread__gt=30)
# 方案2
BookInfo.book.filter(Q(id__gt=3)&Q(bread__gt=30))
```
* 查询id大于3``或者``阅读量大于30的图书信息
```python
BookInfo.book.filter(Q(id__gt=3)|Q(bread__gt=30))
```
* 查询id``不等于``3图书的信息
```python
BookInfo.book.filter(~Q(id=3))
# "负负得正"
BookInfo.book.exclude(~Q(id=3)).values()
```

## 10、order_by
* 查询所有图书的信息，按照id``从小到大``进行排序。
```python
BookInfo.book.all().order_by('id').values()
```
* 查询所有图书的信息，按照id``从大到小``进行排序。
```python
BookInfo.book.all().order_by('-id').values()
```
* 把``id大于3``的图书信息按``阅读量``从大到小排序显示；
```python
BookInfo.book.filter(id__gt=3).order_by('-bread')
```

## 11、聚合函数
* 查询所有图书的数目 select count(*) from booktest_bookinfo;
```python
BookInfo.book.aggregate(Count('id'))
```
* 查询所有图书阅读量的总和
```python
BookInfo.book.aggregate(Sum('bread'))
```
* 统计``id大于3``的所有图书的数目
```python
BookInfo.book.filter(id__gt=3).aggregate(Count('id'))
```
* 显示阅读量最大的书的书名
```python
BookInfo.book.all().order_by('-bread')[0]
```

## 12、查询相关函数返回值总结
```python
get:返回一个对象
all:QuerySet(也就是[])
filter:QuerySet
exclude:QuerySet
order_by:QuerySet
aggregate:字典
count:值
```

## 13、通过对象执行关联查询
* 查询图书id为1的所有英雄信息
```python
b = BookInfo.book.get(id=1)
b.heroInfo_set.all()
```
* 查询id为1的英雄所属图书信息
```python
h = HeroInfo.objects.get(id=1)
h.hbook
h.hbook_id
```

>格式：
1. 由一类的对象查询多类的时候：
```text
一类的对象.多类名小写_set.all() #查询所用数据
```
2. 由多类的对象查询一类的时候：
```text
多类的对象.关联属性 #查询多类的对象对应的一类的对象
```
3. 由多类的对象查询一类对象的id时候：
```text
多类的对象. 关联属性_id
```
## 14、通过模型类事先关联查询
* 查询图书，要求图书中英雄的描述包含``'八'``。Join
```python
BookInfo.objects.filter(heroinfo__hcomment__contains='八')
```
* 查询图书，要求图书中的英雄的id大于3.
```python
BookInfo.objects.filter(heroinfo__id__gt=3)
```
* 查询书名为“天龙八部”的所有英雄。
```python
HeroInfo.objects.filter(hbook__btitle = '天龙八部')
```
>格式
1. 通过多类的条件查询一类的数据：
```text
一类名.objects.filter(多类名小写__多类属性名__条件名=值)
```
2. 通过一类的条件查询多类的数据：
```text
多类名.objects.filter(关联属性__一类属性名__条件名=值)
```
