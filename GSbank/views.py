import os
import random
import string
import time

import PyPDF2
import math
import xlrd
from django.db.models import Q
from django.http import HttpResponseRedirect, FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import FormView, View
import pdfkit
from xhtml2pdf import pisa
# from pdf.forms import MessageForm

# Create your views here.
from GSbank.models import Account, Logs


def index(request):
    return render(request, 'index.html')


# 企业登录
def ee_login(request):
    if request.method == 'POST':
        data = request.POST
        u_password = data.get('u_password')

        user = Account.objects.filter(u_password=u_password)
        if user:
            response = HttpResponseRedirect('/welcome')
            response.set_cookie('user', u_password)
            return response
        else:
            return render(request, 'ee_login.html')
    else:

        return render(request, 'ee_login.html')


def logout(request):
    response = HttpResponseRedirect("/")
    response.delete_cookie("user")
    return response


def account_manage(request):
    u_password = request.COOKIES.get('user')
    print(u_password)
    user = Account.objects.get(u_password=u_password)
    return render(request, 'account_manage/account_manage.html', {'user': user})


def welcome(request):
    u_password = request.COOKIES.get('user')
    print(u_password)
    user = Account.objects.get(u_password=u_password)
    return render(request, 'welcome.html', {'user': user})


def left_money(request):
    u_password = request.COOKIES.get('user')
    print(u_password)
    user = Account.objects.get(u_password=u_password)
    return render(request, 'account_manage/left_money.html', {'user': user})


def detail_query(request):
    u_password = request.COOKIES.get('user')
    print(u_password)
    user = Account.objects.get(u_password=u_password)
    return render(request, 'account_manage/detail_query.html', {"user": user})


def detail_query_result(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    # print(type(a))
    # print(a)
    # print(b)
    start_date = a.replace(',', ' ')
    end_date = b.replace(',', ' ')
    # print(start_date)
    # print(end_date)
    u_password = request.COOKIES.get('user')
    current_user = Account.objects.get(u_password=u_password)
    username = current_user.name
    useraccount = current_user.account_num

    chosed_user = Logs.objects.filter(
        Q(log_account_num=current_user.account_num) & (Q(deal_time__gte=start_date) & Q(deal_time__lte=end_date)))

    return render(request, "account_manage/detail_query_result.html",
                  {'username': username, 'useraccount': useraccount, 'chosed_user': chosed_user})


def electronic_bill(request):
    return render(request, 'account_manage/electronic_bill.html')


def report_query(request):
    return render(request, 'account_manage/report_query.html')


def bank_corp(request):
    return render(request, 'account_manage/bank_corp.html')


def bank_corp_sub(request):
    return render(request, 'account_manage/bank_corp_sub.html')


def query_account(request):
    return render(request, 'account_manage/query_account.html')


def verify(request):
    return render(request, 'account_manage/verify.html')


def reply(request):
    return render(request, 'account_manage/reply.html')


def close_bank_corp(request):
    return render(request, 'account_manage/close_bank_corp.html')


def payment_business(request):
    u_password = request.COOKIES.get('user')
    print(u_password)
    user = Account.objects.get(u_password=u_password)
    return render(request, 'payment_business/payment_business.html', {"user": user})


def onebyone_pay(request):
    u_password = request.COOKIES.get('user')
    user = Account.objects.get(u_password=u_password)
    return render(request, 'payment_business/onebyone_pay.html', {'user': user})


def batch_pay(request):
    return render(request, 'payment_business/batch_pay.html')


def download_template(request):
    file = open('static/files/BatchPay_Template_public.xls', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="BatchPay_Template_public.xls"'
    return response


def order_query(request):
    return render(request, 'payment_business/order_query.html')


def get_person_roll(request):
    return render(request, 'payment_business/get_person_roll.html')


def on_debt(request):
    return render(request, 'account_manage/on_debt.html')


def onebyone_pay_success(request):
    # recieve_name = request.GET.get("recieve_name")
    # recieve_account = request.GET.get("recieve_account")
    # money = request.GET.get("money")
    # u_password = request.COOKIES.get('user')
    # user_give = Account.objects.get(u_password=u_password)
    # user_give.left_money = user_give.left_money - float(money)
    # user_give.save()
    # user_recieve = Account.objects.get(account_num=recieve_account)
    # user_recieve.left_money = user_recieve.left_money + float(money)
    # user_recieve.save()
    #
    # # 设置log
    # now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # # ---------------付款方增加日志----------------
    # logs = Logs()
    # logs.log_account_num = user_give.account_num
    # logs.out_money = money
    # logs.in_money = 0
    # # 查询付款方余额
    # user_give2 = Account.objects.get(u_password=u_password)
    # logs.money_left = user_give2.left_money
    # # 设置对方字段
    # logs.vs_name = recieve_name
    # logs.vs_account = recieve_account
    # # 成交日期
    # logs.deal_time = now_time
    # logs.save()
    #
    # # ----------------收款方增加日志--------------------------
    #
    # logs = Logs()
    # logs.log_account_num = recieve_account
    # logs.out_money = 0
    # logs.in_money = money
    # # 查询收款方余额
    # user_recieve2 = Account.objects.get(account_num=recieve_account)
    # logs.money_left = user_recieve2.left_money
    # # 设置对方字段
    # logs.vs_name = user_give.name
    # logs.vs_account = user_give.account_num
    # # 成交日期
    # logs.deal_time = now_time
    # logs.save()

    return render(request, 'payment_business/onebyone_pay_success.html')


def batch_pay_deal(request):
    if request.method == "POST":
        # 获取普通input标签值，即文件名
        filename = request.POST.get('fileName')
        # 获取file类型的input标签值，即文件内容
        file = request.FILES.get('fileContent')

        data = xlrd.open_workbook(
            filename=None, file_contents=file.read())  # 读取表格
        table = data.sheets()[0]  # 第一张表单
        row = table.nrows
        for i in range(1, row):  # 跳过第0行
            col = table.row_values(i)
            # deal_date = col[1]
            recieve_account = str((col[11]))
            recieve_name = col[12]
            money = float(col[13])
            # print(recieve_account)
            # print(recieve_name)
            # print(money)

            u_password = request.COOKIES.get('user')
            user_give = Account.objects.get(u_password=u_password)
            user_give.left_money = user_give.left_money - money
            user_give.save()
            user_recieve = Account.objects.get(account_num=recieve_account)
            user_recieve.left_money = user_recieve.left_money + money
            user_recieve.save()

            # 设置log
            deal_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # ---------------付款方增加日志----------------
            logs = Logs()
            logs.log_account_num = user_give.account_num
            logs.out_money = money
            logs.in_money = 0
            # 查询付款方余额
            user_give2 = Account.objects.get(u_password=u_password)
            logs.money_left = user_give2.left_money
            # 设置对方字段
            logs.vs_name = recieve_name
            logs.vs_account = recieve_account
            # 成交日期
            logs.deal_time = deal_date
            logs.save()

            # ----------------收款方增加日志--------------------------

            logs = Logs()
            logs.log_account_num = recieve_account
            logs.out_money = 0
            logs.in_money = money
            # 查询收款方余额
            user_recieve2 = Account.objects.get(account_num=recieve_account)
            logs.money_left = user_recieve2.left_money
            # 设置对方字段
            logs.vs_name = user_give.name
            logs.vs_account = user_give.account_num
            # 成交日期
            logs.deal_time = deal_date
            logs.save()

        return JsonResponse({'result': 'ok'})


def batch_pay_success(request):
    return render(request, 'payment_business/batch_pay_success.html')


def IO_category(request):
    return render(request, 'account_manage/IO_category.html')


def asset_flow(request):
    return render(request, 'account_manage/asset_flow.html')


def compete(request):
    return render(request, 'account_manage/compete.html')


# 回单部分
def link_callback(uri, rel):
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
    else:
        return uri

    # 确保本地文件存在
    if not os.path.isfile(path):
        raise Exception(
            "Media URI must start with "
            f"'{settings.MEDIA_URL}' or '{settings.STATIC_URL}'")

    return path


def font_patch():
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from xhtml2pdf.default import DEFAULT_FONT
    pdfmetrics.registerFont(TTFont('yh', '{}/font/msyh.ttf'.format(
        settings.STATICFILES_DIRS[0])))
    DEFAULT_FONT['helvetica'] = 'yh'


# 银行回单
def huidan(request):
    data = request.GET
    date = data.get("date")
    money_out = float(data.get("money_out"))
    money_in = float(data.get("money_in"))
    vs_name = data.get("vs_name")
    vs_account = data.get("vs_account")
    # print(date,money_in,money_out)
    # print(vs_name)
    # print(vs_account)

    u_password = request.COOKIES.get('user')
    current_user = Account.objects.get(u_password=u_password)
    current_user_name = current_user.name

    # 判断谁是收款付款方
    if money_in > 0:
        receive_people = current_user_name
        receive_account = u_password
        pay_people = vs_name
        pay_account = vs_account
    else:
        receive_people = vs_name
        receive_account = vs_account
        pay_people = current_user_name
        pay_account = u_password

    # 打印日期与钱数
    print_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    exchange_maney = money_in if money_in > 0 else money_out
    # 电子回单号码
    elec_num = ''
    for i in range(4):
        seeds = string.digits
        random_str = random.choices(seeds, k=4)
        print("".join(random_str))
        elec_num = elec_num + "".join(random_str) + '-'
    elec_num = elec_num[0:-1]
    # 交易流水号
    seeds = string.digits
    random_str = random.choices(seeds, k=8)
    flow_num = "".join(random_str)
    # 记账网点
    seeds = string.digits
    random_str = random.choices(seeds, k=5)
    net_node = "".join(random_str)
    # 记账柜员
    seeds = string.digits
    random_str = random.choices(seeds, k=5)
    account_make = "".join(random_str)
    # 随机验证码
    er_code = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_'
    for i in range(28):
        a = random.choice(chars)
        er_code += a
    er_code = er_code + '='
    # 金额大写
    big_money = convertNumToChinese(exchange_maney)

    # 开始渲染PDF页面
    context = {"er_code": er_code, "big_money": big_money, "account_make": account_make, "net_node": net_node,
               "flow_num": flow_num, "elec_num": elec_num, "date": date, "exchange_maney": exchange_maney,
               "receive_people": receive_people, "receive_account": receive_account, "pay_people": pay_people,
               "pay_account": pay_account, "print_date": print_date}
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = \
        f"attachment; filename=huidan.pdf"

    html = render_to_string("account_manage/huidan_pdf.html", context=context)
    font_patch()
    status = pisa.CreatePDF(html,
                            dest=response,
                            link_callback=link_callback)

    if status.err:
        return HttpResponse("PDF文件生成失败")

    return response


# 钱数转大写
def convertNumToChinese(totalPrice):
    dictChinese = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖']
    unitChinese = [u'', u'拾', u'佰', u'仟', '', u'拾', u'佰', u'仟']
    # 将整数部分和小数部分区分开
    partA = int(math.floor(totalPrice))
    partB = round(totalPrice - partA, 2)
    strPartA = str(partA)
    strPartB = ''
    if partB != 0:
        strPartB = str(partB)[2:]

    singleNum = []
    if len(strPartA) != 0:
        i = 0
        while i < len(strPartA):
            singleNum.append(strPartA[i])
            i = i + 1
    # 将整数部分先压再出，因为可以从后向前处理，好判断位数
    tnumChinesePartA = []
    numChinesePartA = []
    j = 0
    bef = '0';
    if len(strPartA) != 0:
        while j < len(strPartA):
            curr = singleNum.pop()
            if curr == '0' and bef != '0':
                tnumChinesePartA.append(dictChinese[0])
                bef = curr
            if curr != '0':
                tnumChinesePartA.append(unitChinese[j])
                tnumChinesePartA.append(dictChinese[int(curr)])
                bef = curr
            if j == 3:
                tnumChinesePartA.append(u'萬')
                bef = '0'
            j = j + 1

        for i in range(len(tnumChinesePartA)):
            numChinesePartA.append(tnumChinesePartA.pop())
    A = ''
    for i in numChinesePartA:
        A = A + i
    # 小数部分很简单，只要判断下角是否为零
    B = ''
    if len(strPartB) == 1:
        B = dictChinese[int(strPartB[0])] + u'角'
    if len(strPartB) == 2 and strPartB[0] != '0':
        B = dictChinese[int(strPartB[0])] + u'角' + dictChinese[int(strPartB[1])] + u'分'
    if len(strPartB) == 2 and strPartB[0] == '0':
        B = dictChinese[int(strPartB[0])] + dictChinese[int(strPartB[1])] + u'分'

    if len(strPartB) == 0:
        S = A + u'圆整'
    if len(strPartB) != 0:
        S = A + u'圆' + B
    return S


def huidan_pdfkit(request):
    pdfkit.from_url('http://google.com', 'out.pdf')


# 收款人列表
def payee_list(request):
    u_password = request.COOKIES.get('user')
    try:
        user = Account.objects.get(u_password=u_password)
    except:
        # return render(request, 'index.html')
        data = {
            'code': 308,
            'msg': '身份已失效，请重新登录',
        }
        return JsonResponse(data)
    filter_list = Account.objects.exclude(name__contains=user.name)  # 排除付款人自己
    data_list = []
    for i in filter_list:
        data_list.append({"name": i.name})
    data = {
        'code': 200,
        'msg': '',
        'data_list': data_list,
    }
    return JsonResponse(data)
