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

