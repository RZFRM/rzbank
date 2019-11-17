from django.contrib import admin
from GSbank.models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'account_num', 'left_money', 'bank_type', 'u_password')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('deal_time', 'log_account_num', 'out_money', 'in_money', 'money_left')

# Register your models here.
