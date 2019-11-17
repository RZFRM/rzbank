"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from GSbank.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # 首页
    path('', index),
    # U盾登录
    path('ee_login/', ee_login),
    # path('u_login/',u_login),
    # 登出
    path('logout/', logout),

    # 账户管理
    path('account_manage/', account_manage),
    path('welcome/', welcome),
    path('left_money/', left_money),
    path('on_debt/', on_debt),
    path('detail_query/', detail_query),
    path('detail_query_result/', detail_query_result),
    path('huidan/', huidan),
    path('huidan_pdfkit/', huidan_pdfkit),
    path('IO_category/', IO_category),
    path('asset_flow/', asset_flow),
    path('compete/', compete),
    path('electronic_bill/', electronic_bill),
    path('report_query/', report_query),
    path('bank_corp/', bank_corp),
    path('bank_corp_sub/', bank_corp_sub),
    path('query_account/', query_account),
    path('verify/', verify),
    path('reply/', reply),
    path('close_bank_corp/', close_bank_corp),
    url('payee_list/', payee_list),  # 收款人名册

    # 支付业务
    path('payment_business/', payment_business),
    path('onebyone_pay/', onebyone_pay),
    path('batch_pay/', batch_pay),
    path('order_query/', order_query),
    path('get_person_roll/', get_person_roll),
    path('onebyone_pay_success/', onebyone_pay_success),
    path('batch_pay_deal/', batch_pay_deal),
    path('batch_pay_success/', batch_pay_success),
    # 下载批量处理模板
    path('download_template/', download_template),

]
