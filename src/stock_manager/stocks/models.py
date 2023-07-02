from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField('材料名', max_length=32)
    amount = models.CharField('内容量', max_length=32)
    stock_type = models.IntegerField('種類')
    stock_num = models.IntegerField('在庫数')
    remarks = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name
