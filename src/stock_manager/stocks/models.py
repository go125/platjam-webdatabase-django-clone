from django.conf import settings
from django.db import models

# Create your models here.

class Stock(models.Model):
    class StockType(models.IntegerChoices):
        BREAD = 1
        FRUITS = 2
        SEASONING = 3
        JAPANESE_SWEETS = 4

    name = models.CharField('材料名', max_length=32)
    amount = models.CharField('内容量', max_length=32)
    stock_type = models.IntegerField('種類', choices=StockType.choices)
    stock_num = models.PositiveIntegerField('在庫数', default = 0)
    managed_by = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="材料管理者",on_delete=models.PROTECT)
    remarks = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name
