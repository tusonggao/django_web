from django.db import models
from sqlalchemy import create_engine


class RecommendItemInfo(models.Model):
    num = models.IntegerField(verbose_name='序号')
    product_code = models.CharField(max_length=12,  verbose_name='商品编号')
    product_name = models.CharField(max_length=100, verbose_name='商品名称')

    product_class_code = models.CharField(max_length=12, verbose_name='类别编码')
    product_class_name = models.CharField(max_length=16, verbose_name='类别名称')

    product_price = models.FloatField(verbose_name='商品价格')
    amount = models.IntegerField(verbose_name='半年销量')
    product_url = models.CharField(max_length=50, verbose_name='商品链接')

    def __str__(self):
        return "{}-{}".format(self.product_code, self.product_name)

    class Meta:
        verbose_name = '推荐商品信息'


if __name__=='__main__':
    print('hello world!')




