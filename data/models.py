from django.utils import timezone
from django.contrib import admin
from django.db import models
import datetime


# Create your models here.

# ssq
class SsqModel(models.Model):
    # ...
    def __str__(self):
        return self.qiCi + self.kaiJiangRiQi.__str__()

    qiCi = models.CharField(max_length=20)
    kaiJiangRiQi = models.CharField(max_length=20)
    # 红球1-6 蓝球
    hongYi = models.IntegerField(default=0)
    hongEr = models.IntegerField(default=0)
    hongSan = models.IntegerField(default=0)
    hongSi = models.IntegerField(default=0)
    hongWu = models.IntegerField(default=0)
    hongLiu = models.IntegerField(default=0)
    langQiu = models.IntegerField(default=0)
    # 奖池金额
    jiangChiJinEr = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    # 一等奖 注数、资金
    yiDengJiangZhuShu = models.IntegerField(default=0)
    yiDengJiangJiangJin = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    # 二等奖 注数、资金
    erDengJiangZhuShu = models.IntegerField(default=0)
    erDengJiangJiangJin = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    @admin.display(
        boolean=True,
        ordering='kaiJiangRiQi',
        description='开奖日期?',
    )
    def was_kaijiangriqi_recently(self):
        # return self.pub_date >= timezone.now()
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.kaiJiangRiQi <= now

