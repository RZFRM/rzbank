from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=32)
    account_num = models.CharField(max_length=32)
    u_password = models.CharField(max_length=32)
    left_money = models.IntegerField()
    bank_type = models.CharField(max_length=32)


class Logs(models.Model):
    deal_time = models.DateTimeField()
    log_account_num = models.CharField(max_length=32)
    out_money = models.IntegerField()  # 转出账户的转出额
    in_money = models.IntegerField()  # 转入账户的转入额
    money_left = models.IntegerField()
    vs_name = models.CharField(max_length=32)
    vs_account = models.CharField(max_length=32)

# Create your models here.
