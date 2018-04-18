from django.db import models


# Create your models here.
class Article(models.Model):
    # 标题
    title = models.CharField(max_length=30, default='无标题')
    # 内容
    content = models.TextField(null=True)
