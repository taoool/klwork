from django.shortcuts import render, redirect, HttpResponse
from klzg import models
from klzg.models import CustomerCollection, Customer, Sales, Salesman, Pay, Department, Commission, FinishPay
import re
from django.db.models import Q, Sum

# Create your views here.
def index(request):
    """导航页"""

    return render(request, "index.html")


def customer_inf(request):
    """客户信息"""
    ret = models.Customer.objects.all()
    if request.method == "POST":
        sea = request.POST.get("search_cus")
        ret = models.Customer.objects.filter(name__contains=sea).all()
    return render(request, "customer_inf.html", {"ret": ret})

def modify_customer_inf(request, **kwargs):
    """客户信息表-增改"""
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = Customer.objects.filter(id=cus_id).first()
    if request.method == "POST":
        cus = request.POST.get("customer")
        if kwargs:
            cus_id = kwargs.get("cus_id")
            upt = Customer.objects.filter(id=cus_id).update(name=cus)
        else:
            customer_obj = Customer.objects.create(name=cus)
        return redirect("/customer_inf/")
    return render(request, "add_customer_inf.html", locals())

def delete_customer_inf(request, cus_id):
    """客户信息表-删除"""
    cus_obj = Customer.objects.filter(id=cus_id).first().delete()
    return redirect("/customer_inf/")


def customer(request):
    """客户收款详情"""
    ret = models.CustomerCollection.objects.all()
    if request.method == "POST":
        sea = request.POST.get("search_cus")
        ret = models.CustomerCollection.objects.filter(customer__name__contains=sea).all()
    return render(request, "customer.html", {"ret": ret})

def modify_customer(request, **kwargs):
    """客户收款表-增改"""
    cus = models.Customer.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = CustomerCollection.objects.filter(id=cus_id).first()
    if request.method == "POST":
        cus = request.POST.get("customer")
        a = Customer.objects.filter(name=cus).first()
        contact = request.POST.get("contact")
        remark = request.POST.get("remark")
        account = request.POST.get("account")
        account_method = request.POST.get("account_method")
        account_number = request.POST.get("account_number")

        if kwargs:
            cus_id = kwargs.get("cus_id")
            cuscol_obj = CustomerCollection.objects.filter(id=cus_id).update(name=contact, remark=remark, account_name=account, account_method=account_method, account_number=account_number,customer=a.id)
        else:
            cuscol_obj = CustomerCollection.objects.create(name=contact, remark=remark, account_name=account, account_method=account_method, account_number=account_number, customer_id=a.id)
        return redirect("/customer/")
    return render(request, "add_customer.html", locals())

def delete_customer(request, cus_id):
    """客户收款表-删除"""
    cus_obj = CustomerCollection.objects.filter(id=cus_id).first().delete()
    return redirect("/customer/")


def salesman(request):
    """业务员信息详情"""
    ret = models.Salesman.objects.all()
    if request.method == "POST":
        search_obj = request.POST.get("search")
        ret = models.Salesman.objects.filter(name__contains=search_obj).all()
    return render(request, "salesman.html", {'ret': ret})

def modify_salesman(request, **kwargs):
    """业务员信息-增改"""
    cus = models.Department.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = models.Salesman.objects.filter(id=cus_id).first()

    if request.method == "POST":
        name = request.POST.get("salesman")
        department = request.POST.get("department")
        a = Department.objects.filter(name=department).first()

        if kwargs:
            cus_id = kwargs.get("cus_id")
            sal_obj = Salesman.objects.filter(id=cus_id).update(name=name, department_id=a.id)
        else:
            sal_obj = Salesman.objects.create(name=name, department_id=a.id)
        return redirect("/salesman/")
    return render(request, "add_salesman.html", locals())

def delete_salesman(request, cus_id):
    """业务员信息-删除"""
    sal_obj = Salesman.objects.filter(id=cus_id).delete()
    return redirect("/salesman/")


def project(request, **kwargs):
    """支付项目表"""
    ret = models.Pay.objects.all()
    opt = models.Pay.objects.values("start_time").distinct().all()
    # for foo in opt:
    #     print(foo.get("time"))
    if kwargs:
        time_id = kwargs.get("time_id")
        time_id += "-01 01:01:01"
        ret = models.Pay.objects.filter(start_time=time_id).all()
    if request.method == "POST":
        sea = request.POST.get("cus_name")
        ret = models.Pay.objects.filter(customercol__customer__name__contains=sea).all()
    return render(request, "project.html", {"ret": ret, "opt": opt})

def modify_project(request, **kwargs):
    """支付项目-增改"""
    cus = models.CustomerCollection.objects.all()
    sal = models.Salesman.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = models.Pay.objects.filter(id=cus_id).first()
    if request.method == "POST":
        cu = request.POST.get("customer")
        co = request.POST.get("contact")
        con = CustomerCollection.objects.filter(Q(customer__name=cu) & Q(name=co)).first()
        sal = request.POST.get("salesman")
        sale = Salesman.objects.filter(name=sal).first()
        price = request.POST.get("price")
        stime = request.POST.get("start_time")
        etime = request.POST.get("end_time")
        stime += "-01 01:01:01"
        etime += "-01 01:01:01"
        if kwargs:
            cus_id = kwargs.get("cus_id")
            pay_obj = Pay.objects.filter(id=cus_id).update(start_time=stime, end_time=etime, price=price, customercol_id=con.id, salesman_id=sale.id)
        else:
            pay_obj = Pay.objects.create(start_time=stime, end_time=etime, price=price, customercol_id=con.id, salesman_id=sale.id)
        return redirect("/project/")

    return render(request, "add_project.html", locals())

def delete_project(request, cus_id):
    """支付项目-删除"""
    pay_obj = Pay.objects.filter(id=cus_id).delete()
    return redirect("/project/")


def commission(request, **kwargs):
    """提成表"""
    ret = models.Commission.objects.all()
    opt = models.Commission.objects.values("sales__time").distinct().all()
    # for foo in opt:
    #     print(foo.get("time"))
    if kwargs.get("year_id"):
        # print("123")
        year = kwargs.get("year_id")
        ret = models.Commission.objects.filter(Q(sales__time__year=year)).all()
    if kwargs.get("month_id"):
        # print("456")
        year = kwargs.get("year_on")
        month = kwargs.get("month_id")
        ret = models.Commission.objects.filter(Q(sales__time__year=year), Q(sales__time__month=month)).all()
    to = ret.aggregate(Sum("total"))
    tol=to["total__sum"]
    if request.method == "POST":
        sea = request.POST.get("cus_name")
        ret = models.Commission.objects.filter(pay__customercol__customer__name__contains=sea).all()
    # return render(request, "pay.html", {"ret": ret, "opt": opt, "tol": tol})
    return render(request, "pay.html", locals())

def modify_commission(request, **kwargs):
    """提成表-增改"""
    cus = models.Customer.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = Commission.objects.filter(id=cus_id).first()
    if request.method == "POST":
        order = request.POST.get("order")  # 订单号
        time = request.POST.get("time")
        num = request.POST.get("number")
        pri = models.Pay.objects.filter(id=order).first()
        price = pri.price
        total = int(num) * float(price)
        time += "-01 01:01:01"
        if kwargs:
            cus_id = kwargs.get("cus_id")
            ret = Commission.objects.filter(id=cus_id).first()
            sal_obj = Sales.objects.filter(id=ret.sales_id).update(time=time, number=num)
            com_obj = Commission.objects.filter(id=cus_id).update(total=total, pay_id=order)
        else:
            sal_obj = Sales.objects.create(time=time, number=num)
            com_obj = Commission.objects.create(total=total, pay_id=order, sales_id=sal_obj.id)
        return redirect("/commission/")
    return render(request, "add_pay.html", locals())

def delete_commission(request, cus_id):
    """提成表-删除"""
    com_obj = Commission.objects.filter(id=cus_id).delete()
    # print("1111111")
    return redirect("/commission/")

def commission_flash(request):
    """提成表-刷新"""
    ret = Commission.objects.all().values_list("id")

    for i in ret:
        nu = models.Commission.objects.filter(id=i[0]).all()
        for cc in nu:
            num = cc.sales.number
            price = cc.pay.price
            total = int(num) * float(price)
            com_obj = Commission.objects.filter(id=i[0]).update(total=total)

    return redirect("/commission/")

def commission_detail(request, **kwargs):
    """提成表-详细"""
    cu = kwargs.get("customer_name")
    ret = models.Commission.objects.filter(pay__customercol__customer__name=cu).all()
    opt = models.Commission.objects.values("sales__time").distinct().all()
    a = ret.values("pay__customercol__customer__name")
    b = a[0]["pay__customercol__customer__name"]
    if kwargs.get("year_id"):
        # print("++++")
        year = kwargs.get("year_id")
        ret = ret.filter(sales__time__year=year).all()
    if kwargs.get("month_id"):
        # print("456")
        year = kwargs.get("year_on")
        month = kwargs.get("month_id")
        ret = ret.filter(Q(sales__time__year=year), Q(sales__time__month=month)).all()
    to = ret.aggregate(Sum("total"))
    tol=to["total__sum"]
    return render(request, "pay_detail.html", locals())

def add_commission_detail(request, customer_name):
    """提成详细表-增"""
    cus = models.Customer.objects.all()
    ret = Commission.objects.filter(pay__customercol__customer__name=customer_name).first()
    if request.method == "POST":
        order = request.POST.get("order")  # 订单号
        time = request.POST.get("time")
        pay_obj = Pay.objects.filter(id=order).values("price")
        price = pay_obj[0]["price"]
        # print(price)
        num = request.POST.get("number")
        remark = request.POST.get("remark")
        if not remark:
            remark = "未付"
        total = int(num) * float(price)
        time += "-01 01:01:01"
        sal_obj = Sales.objects.create(time=time, number=num)
        com_obj = Commission.objects.create(total=total, pay_id=order, sales_id=sal_obj.id, remark=remark)
        a = Commission.objects.filter(pay__customercol__customer__name=customer_name).values("pay__customercol__customer__name")
        b = a[0]["pay__customercol__customer__name"]
        return redirect("/commission/" + b)
    return render(request, "add_pay_detail.html", locals())

def modify_commission_detail(request, cus_id):
    """提成详细表-改"""
    cus = models.Customer.objects.all()
    ret = Commission.objects.filter(id=cus_id).first()
    if request.method == "POST":
        order = request.POST.get("order")  # 订单号
        time = request.POST.get("time")
        num = request.POST.get("number")
        price = request.POST.get("price")
        remark = request.POST.get("remark")
        total = int(num) * float(price)
        time += "-01 01:01:01"
        ret = Commission.objects.filter(id=cus_id).first()
        sal_obj = Sales.objects.filter(id=ret.sales_id).update(time=time, number=num)
        pay_obj = Pay.objects.filter(id=ret.pay_id).update(price=price)
        com_obj = Commission.objects.filter(id=cus_id).update(total=total, pay_id=order, remark=remark)
        a = Commission.objects.filter(id=cus_id).values("pay__customercol__customer__name")
        b = a[0]["pay__customercol__customer__name"]
        # print(b)
        return redirect("/commission/" + b)
    return render(request, "modify_pay_detail.html", locals())

# def commission_flash_detail(request, cus_id):
#     """提成表-刷新"""
#     na = Commission.objects.filter(id=cus_id).values("pay__customercol__customer__name")
#     name = na[0]["pay__customercol__customer__name"]
#     print(cus_id)
#     return redirect("/commission/" + name + "/")

def delete_commission_detail(request, cus_id):
    """提成表-删除"""
    # print("2222222")
    na = Commission.objects.filter(id=cus_id).values("pay__customercol__customer__name")
    name = na[0]["pay__customercol__customer__name"]
    com_obj = Commission.objects.filter(id=cus_id).delete()

    return redirect("/commission/" + name + "/")


def finish(request, **kwargs):
    """付款记录表"""
    ret = models.FinishPay.objects.all()
    opt = models.FinishPay.objects.values("time").distinct().all()
    # for foo in opt:
    #     print(foo.get("time"))
    if kwargs:
        time_id = kwargs.get("time_id")
        time_id += "-01 01:01:01"
        ret = models.FinishPay.objects.filter(time=time_id).all()
    if request.method == "POST":
        sea = request.POST.get("cus_name")
        ret = models.FinishPay.objects.filter(customercol__customer__name__contains=sea).all()
    return render(request, "finish.html", {"ret": ret, "opt": opt})

def modify_finish(request, **kwargs):
    """付款记录表-增改"""
    cus = models.CustomerCollection.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = FinishPay.objects.filter(id=cus_id).first()
    if request.method == "POST":
        con = request.POST.get("contact")
        a = CustomerCollection.objects.filter(name=con).first()
        time = request.POST.get("pay_time")
        money = request.POST.get("money")
        method = request.POST.get("pay_method")
        account = request.POST.get("account_number")
        remark = request.POST.get("remark")
        time += "-01 01:01:01"

        if kwargs:
            cus_id = kwargs.get("cus_id")
            fin_obj = FinishPay.objects.filter(id=cus_id).update(time=time, money=money, payment_method=method, account_number=account, remark=remark, customercol_id=a.id)
        else:
            fin_obj = FinishPay.objects.create(time=time, money=money, payment_method=method, account_number=account, remark=remark, customercol_id=a.id)
        return redirect("/finish/")
    return render(request, "add_finish.html", locals())

def delete_finish(request, cus_id):
    """付款记录表-删除"""
    fin_obj = FinishPay.objects.filter(id=cus_id).delete()
    return redirect("/finish/")


def department(request):
    """部门表"""
    ret = models.Department.objects.all()
    if request.method == "POST":
        sea = request.POST.get("search")
        ret = models.Department.objects.filter(name__contains=sea).all()
    return render(request, "department.html", {"ret": ret})

def modify_department(request, **kwargs):
    """部门表-增改"""
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = models.Department.objects.filter(id=cus_id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        if kwargs:
            cus_id = kwargs.get("cus_id")
            dep_obj = Department.objects.filter(id=cus_id).update(name=name)
        else:
            dep_obj = Department.objects.create(name=name)
        return redirect("/department/")
    return render(request, "add_department.html", locals())

def delete_department(request, cus_id):
    """部门表-删除"""
    ret = Department.objects.filter(id=cus_id).delete()
    return redirect("/department/")





def aba(request, **kwargs):
    """测试用"""
    opt = models.Commission.objects.values("sales__time").distinct().all()

    opt = models.Pay.objects.values("start_time").distinct().all()


    ret = models.Commission.objects.all()
    if kwargs:
        year = kwargs.get("year_id")
        ret = models.Commission.objects.filter(sales__time__year=year).all()
        print("1231")
    if request.method == "POST":
        sea = request.POST.get("cus_name")
        ret = models.Commission.objects.filter(pay__customercol__customer__name__contains=sea).all()
    return render(request, "123.html", {"ret": ret, "opt": opt})