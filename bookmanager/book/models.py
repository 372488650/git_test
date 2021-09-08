from django.db import models

# Create your models here.


class BookInfo(models.Model):
    # Id
    name = models.CharField(max_length=10)


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外健约束：人物属于那本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
