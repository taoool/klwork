from django.shortcuts import render, redirect
import xlrd
from excel import models
from excel.models import History
from klzg.models import CustomerCollection, Customer, Sales, Salesman, Pay, Department, Commission, FinishPay
from django.http import JsonResponse
from klwork.settings import MEDIA_ROOT
from django.db.models import Q

# Create your views here.


def history(request):
    """历史记录"""
    his = models.History.objects.all()
    time = his.first()

    response={"user": None}
    if request.is_ajax():
        avatar_obj = request.FILES.get("avatar")
        # print(avatar_obj)
        if avatar_obj:
            History.objects.create(file_name=avatar_obj)
            file_name = (MEDIA_ROOT + "\\avatars\\" + str(avatar_obj))
            if file_name:
                ws = xlrd.open_workbook(file_name)
                ws.sheet_names()
                # print("sheets：" + str(ws.sheet_names()))
                table2 = ws.sheets()[1]

                # 表2
                for i in range(1, table2.nrows):
                    cell_sal = table2.cell(i, 0).value  # 业务员
                    cell_cus = table2.cell(i, 1).value  # 客户
                    cell_con = table2.cell(i, 2).value  # 联络人
                    cell_rem = table2.cell(i, 3).value  # 备注
                    cell_pri = table2.cell(i, 4).value  # 金额
                    cell_sti = xlrd.xldate_as_datetime(table2.cell(i, 5).value, 5).strftime("%Y-%m")  # 开始时间
                    cell_sti += "-01 01:01:01"
                    cell_eti = xlrd.xldate_as_datetime(table2.cell(i, 6).value, 6).strftime("%Y-%m")  # 结束时间
                    cell_eti += "-01 01:01:01"
                    cell_acc = table2.cell(i, 7).value  # 收款人
                    cell_met = table2.cell(i, 8).value  # 开户行
                    cell_num = table2.cell(i, 9).value  # 收款账号

                    # 存储客户
                    ret = Customer.objects.filter(name=cell_cus).all().exists()
                    if not ret:
                        # print("error")
                        Customer.objects.create(name=cell_cus)
                    cud = Customer.objects.filter(name=cell_cus).first()

                    # 存储客户收款人
                    cuc = CustomerCollection.objects.filter(Q(name=cell_con), Q(account_name=cell_acc)).all().exists()
                    if not cuc:
                        CustomerCollection.objects.create(name=cell_con, remark=cell_rem, account_name=cell_acc, account_method=cell_met, account_number=cell_num, customer_id=cud.id)
                    cuds = CustomerCollection.objects.filter(Q(name=cell_con), Q(customer_id=cud.id)).first()

                    # 存储支付项目
                    pro = Pay.objects.filter(Q(customercol_id=cuds.id), Q(start_time=cell_sti)).all().exists()
                    sman = Salesman.objects.filter(name=cell_sal).first()
                    if pro:
                        Pay.objects.filter(Q(customercol_id=cuds.id), Q(start_time=cell_sti)).update(end_time=cell_eti, price=cell_pri, salesman_id=sman.id)
                    else:
                        Pay.objects.filter(Q(customercol_id=cuds.id), Q(start_time=cell_sti)).create(start_time=cell_sti, end_time=cell_eti, price=cell_pri, customercol_id=cuds.id, salesman_id=sman.id)

                # 表1
                table1 = ws.sheets()[0]
                for i in range(1, table1.nrows):
                    cell_tim = xlrd.xldate_as_datetime(table1.cell(i, 0).value, 0).strftime("%Y-%m")  # 时间
                    cell_tim += "-01 01:01:01"
                    print(cell_tim)
                    cell_name = table1.cell(i, 1).value  # 客户
                    cell_number = table1.cell(i, 2).value  # 数量
                    # print(cell_tim, end="    ")
                    # print(cell_name, end="    ")
                    # print(cell_number)

                    c = Customer.objects.filter(name=cell_name).first()
                    a = Sales.objects.create(time=cell_tim, number=cell_number, customer_id=c.id)
                    b = Pay.objects.filter(Q(customercol__customer__name=cell_name), Q(start_time__lt=cell_tim), Q(end_time__gt=cell_tim)).all()
                    for bb in b:
                        total = int(a.number) * int(bb.price)
                        Commission.objects.create(total=total, pay_id=bb.id, sales_id=a.id)

        return JsonResponse(response)
    return render(request, "history.html", {"his": his, "time": time})
