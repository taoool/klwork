from django.shortcuts import render, redirect, HttpResponse
from klzg import models
from klzg.models import CustomerCollection, Customer, Sales, Salesman, Pay, Department, Commission, FinishPay
from django.core.paginator import Paginator, EmptyPage
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

    paginator = Paginator(ret, 10)
    # print("page_range", paginator.page_range)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "customer_inf.html", locals())

def modify_customer_inf(request, **kwargs):
    """客户信息表-增改"""
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = Customer.objects.filter(id=cus_id).first()
    if request.method == "POST":
        cus = request.POST.get("customer")
        if kwargs:
            cus_id = kwargs.get("cus_id")
            try:
                upt = Customer.objects.filter(id=cus_id).update(name=cus)
            except:
                return render(request, "not_found.html")
        else:
            try:
                customer_obj = Customer.objects.create(name=cus)
            except:
                return render(request, "not_found.html")
        return redirect("/customer_inf/")
    return render(request, "add_customer_inf.html", locals())

def delete_customer_inf(request, cus_id):
    """客户信息表-删除"""
    try:
        cus_obj = Customer.objects.filter(id=cus_id).first().delete()
    except:
        return render(request, "not_found.html")
    return redirect("/customer_inf/")


def customer(request):
    """客户收款详情"""
    ret = models.CustomerCollection.objects.all()
    if request.method == "POST":
        sea = request.POST.get("search_cus")
        ret = models.CustomerCollection.objects.filter(customer__name__contains=sea).all()

    paginator = Paginator(ret, 5)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "customer.html", locals())

def modify_customer(request, **kwargs):
    """客户收款表-增改"""
    cus = models.Customer.objects.all()
    ret = CustomerCollection.objects.all()
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
            try:
                cuscol_obj = CustomerCollection.objects.filter(id=cus_id).update(name=contact, remark=remark, account_name=account, account_method=account_method, account_number=account_number, customer=a.id)
            except:
                return render(request, "not_found.html")
        else:
            try:
                cuscol_obj = CustomerCollection.objects.create(name=contact, remark=remark, account_name=account, account_method=account_method, account_number=account_number, customer_id=a.id)
            except:
                return render(request, "not_found.html")
        return redirect("/customer/")
    return render(request, "add_customer.html", locals())

def delete_customer(request, cus_id):
    """客户收款表-删除"""
    try:
        cus_obj = CustomerCollection.objects.filter(id=cus_id).first().delete()
    except:
        return render(request, "not_found.html")
    return redirect("/customer/")


def salesman(request):
    """业务员信息详情"""
    ret = models.Salesman.objects.all()
    if request.method == "POST":
        search_obj = request.POST.get("search")
        ret = models.Salesman.objects.filter(name__contains=search_obj).all()

    paginator = Paginator(ret, 10)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "salesman.html", locals())

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
            try:
                sal_obj = Salesman.objects.filter(id=cus_id).update(name=name, department_id=a.id)
            except:
                return render(request, "not_found.html")
        else:
            try:
                sal_obj = Salesman.objects.create(name=name, department_id=a.id)
            except:
                return render(request, "not_found.html")
        return redirect("/salesman/")
    return render(request, "add_salesman.html", locals())

def delete_salesman(request, cus_id):
    """业务员信息-删除"""
    try:
        sal_obj = Salesman.objects.filter(id=cus_id).delete()
    except:
        return render(request, "not_found.html")
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

    paginator = Paginator(ret, 10)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "project.html", locals())

def modify_project(request, **kwargs):
    """支付项目-增改"""
    cus = models.CustomerCollection.objects.all()
    sal = models.Salesman.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = models.Pay.objects.filter(id=cus_id).first()
    if request.method == "POST":
        cu = request.POST.get("customer")
        # print(cu.split("\xa0\xa0\xa0\xa0", 3))
        co = cu.split("\xa0\xa0\xa0\xa0", 3)
        con = CustomerCollection.objects.filter(Q(customer__name=co[1]) & Q(name=co[2])).first()
        sal = request.POST.get("salesman")
        sale = Salesman.objects.filter(name=sal).first()
        price = request.POST.get("price")
        stime = request.POST.get("start_time")
        etime = request.POST.get("end_time")
        stime += "-01 01:01:01"
        etime += "-01 01:01:01"
        if kwargs:
            cus_id = kwargs.get("cus_id")
            try:
                pay_obj = Pay.objects.filter(id=cus_id).update(start_time=stime, end_time=etime, price=price, customercol_id=con.id, salesman_id=sale.id)
            except:
                return render(request, "not_found.html")
        else:
            try:
                pay_obj = Pay.objects.create(start_time=stime, end_time=etime, price=price, customercol_id=con.id, salesman_id=sale.id)
            except:
                return render(request, "not_found.html")
        return redirect("/project/")
    return render(request, "add_project.html", locals())

def delete_project(request, cus_id):
    """支付项目-删除"""
    try:
        pay_obj = Pay.objects.filter(id=cus_id).delete()
    except:
        return render(request, "not_found.html")
    return redirect("/project/")


def commission(request, **kwargs):
    """提成表"""
    ret = models.Commission.objects.all()
    note = models.FinishPay.objects.all()
    opt = models.Commission.objects.values("sales__time").distinct().all()
    # 待付
    mon = note.aggregate(Sum("money"))
    mony = -mon["money__sum"]
    ds = ret.aggregate(Sum("total"))
    dss=ds["total__sum"]
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

    if request.method == "POST":
        sea = request.POST.get("cus_name")
        ret = models.Commission.objects.filter(pay__customercol__customer__name__contains=sea).all()
    # 总额
    to = ret.aggregate(Sum("total"))
    tol=to["total__sum"]

    paginator = Paginator(ret, 9)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "pay.html", locals())

def modify_commission(request, **kwargs):
    """提成表-增改"""
    cus = models.Customer.objects.all()
    pay = models.Pay.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = Commission.objects.filter(id=cus_id).first()
    if request.method == "POST":
        ord = request.POST.get("order")  # 订单号
        order = ord.split("\xa0", 1)[0]
        cusname = ord.split("\xa0\xa0\xa0\xa0", 2)[1]  # 客户名字
        cust = Customer.objects.filter(name=cusname).first()
        # print(order)
        time = request.POST.get("time")
        num = request.POST.get("number")
        pri = models.Pay.objects.filter(id=order).first()
        price = pri.price
        total = int(num) * float(price)
        time += "-01 01:01:01"
        if kwargs:
            cus_id = kwargs.get("cus_id")
            ret = Commission.objects.filter(id=cus_id).first()
            try:
                sal_obj = Sales.objects.filter(id=ret.sales_id).update(time=time, number=num, customer_id=cust.id)
                com_obj = Commission.objects.filter(id=cus_id).update(total=total, pay_id=order)
            except:
                return render(request, "not_found.html")
        else:
            try:
                sal_obj = Sales.objects.create(time=time, number=num, customer_id=cust.id)
                com_obj = Commission.objects.create(total=total, pay_id=order, sales_id=sal_obj.id)
            except:
                return render(request, "not_found.html")
        return redirect("/commission/")
    return render(request, "add_pay.html", locals())

def delete_commission(request, cus_id):
    """提成表-删除"""
    try:
        com_obj = Commission.objects.filter(id=cus_id).delete()
    except:
        return render(request, "not_found.html")
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
        year = kwargs.get("year_id")
        ret = ret.filter(sales__time__year=year).all()
    if kwargs.get("month_id"):
        year = kwargs.get("year_on")
        month = kwargs.get("month_id")
        ret = ret.filter(Q(sales__time__year=year), Q(sales__time__month=month)).all()
    # 总额
    to = ret.aggregate(Sum("total"))
    tol = to["total__sum"]
    # 待付
    noo = ret.aggregate(Sum("money"))
    note = noo["money__sum"]
    paid = int(tol) - int(note)

    paginator = Paginator(ret, 9)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "pay_detail.html", locals())

def add_commission_detail(request, customer_name):
    """提成详细表-增"""
    cus = models.Customer.objects.all()
    ret = Commission.objects.filter(pay__customercol__customer__name=customer_name).first()
    pay = models.Pay.objects.all()
    if request.method == "POST":
        ord = request.POST.get("order")  # 订单号
        order = ord.split("\xa0", 1)[0]
        cusname = ord.split("\xa0\xa0\xa0\xa0", 2)[1]  # 客户名字
        cust = Customer.objects.filter(name=cusname).first()
        time = request.POST.get("time")
        pay_obj = Pay.objects.filter(id=order).values("price")
        price = pay_obj[0]["price"]
        # print(price)
        num = request.POST.get("number")
        total = int(num) * float(price)
        time += "-01 01:01:01"
        try:
            sal_obj = Sales.objects.create(time=time, number=num, customer_id=cust.id)
            com_obj = Commission.objects.create(total=total, pay_id=order, sales_id=sal_obj.id)
        except:
            return render(request, "not_found.html")
        a = Commission.objects.filter(pay__customercol__customer__name=customer_name).values("pay__customercol__customer__name")
        b = a[0]["pay__customercol__customer__name"]
        return redirect("/commission/" + b)
    return render(request, "add_pay_detail.html", locals())

def modify_commission_detail(request, cus_id):
    """提成详细表-改"""
    cus = models.Customer.objects.all()
    ret = Commission.objects.filter(id=cus_id).first()
    pay = models.Pay.objects.all()
    if request.method == "POST":
        ord = request.POST.get("order")  # 订单号
        order = ord.split("\xa0", 1)[0]
        cusname = ord.split("\xa0\xa0\xa0\xa0", 2)[1]  # 客户名字
        cust = Customer.objects.filter(name=cusname).first()
        time = request.POST.get("time")
        num = request.POST.get("number")
        price = request.POST.get("price")
        money = request.POST.get("money")
        total = int(num) * float(price)
        # print(num)
        # print(price)
        # print(total)
        time += "-01 01:01:01"
        ret = Commission.objects.filter(id=cus_id).first()
        try:
            sal_obj = Sales.objects.filter(id=ret.sales_id).update(time=time, number=num, customer_id=cust.id)
            pay_obj = Pay.objects.filter(id=ret.pay_id).update(price=price)
            com_obj = Commission.objects.filter(id=cus_id).update(total=total, pay_id=order, money=money)
        except:
            return render(request, "not_found.html")
        a = Commission.objects.filter(id=cus_id).values("pay__customercol__customer__name")
        b = a[0]["pay__customercol__customer__name"]
        # print(b)
        return redirect("/commission/" + b)
    return render(request, "modify_pay_detail.html", locals())

def delete_commission_detail(request, cus_id):
    """提成表-删除"""
    # print("2222222")
    na = Commission.objects.filter(id=cus_id).values("pay__customercol__customer__name")
    name = na[0]["pay__customercol__customer__name"]
    try:
        com_obj = Commission.objects.filter(id=cus_id).delete()
    except:
        return render(request, "not_found.html")
    return redirect("/commission/" + name + "/")


def finish(request, **kwargs):
    """付款记录表"""
    ret = models.FinishPay.objects.all()
    opt = models.FinishPay.objects.values("time").distinct().all()

    if kwargs:
        time_id = kwargs.get("time_id")
        time_id += "-01 01:01:01"
        ret = models.FinishPay.objects.filter(time=time_id).all()
    if request.method == "POST":
        sea = request.POST.get("cus_name")
        ret = models.FinishPay.objects.filter(customercol__customer__name__contains=sea).all()
    to = ret.aggregate(Sum("money"))
    tol = to["money__sum"]
    return render(request, "finish.html", {"ret": ret, "opt": opt, "tol": tol})

def modify_finish(request, **kwargs):
    """付款记录表-增改"""
    cus = models.CustomerCollection.objects.all()
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = FinishPay.objects.filter(id=cus_id).first()
    if request.method == "POST":
        con = request.POST.get("customer")
        con = con.split("\xa0\xa0\xa0\xa0", 2)
        a = CustomerCollection.objects.filter(id=con[0]).first()
        time = request.POST.get("pay_time")
        money = request.POST.get("money")
        method = request.POST.get("pay_method")
        account = request.POST.get("account_number")
        remark = request.POST.get("remark")
        time += "-01 01:01:01"
        if kwargs:
            cus_id = kwargs.get("cus_id")
            try:
                fin_obj = FinishPay.objects.filter(id=cus_id).update(time=time, money=money, payment_method=method, account_number=account, remark=remark, customercol_id=a.id)
            except:
                return render(request, "not_found.html")
        else:
            try:
                fin_obj = FinishPay.objects.create(time=time, money=money, payment_method=method, account_number=account, remark=remark, customercol_id=a.id)
            except:
                return render(request, "not_found.html")
        return redirect("/finish/")
    return render(request, "add_finish.html", locals())

def delete_finish(request, cus_id):
    """付款记录表-删除"""
    try:
        fin_obj = FinishPay.objects.filter(id=cus_id).delete()
    except:
        return render(request, "not_found.html")
    return redirect("/finish/")


def department(request):
    """部门表"""
    ret = models.Department.objects.all()
    if request.method == "POST":
        sea = request.POST.get("search")
        ret = models.Department.objects.filter(name__contains=sea).all()

    paginator = Paginator(ret, 10)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "department.html", locals())

def modify_department(request, **kwargs):
    """部门表-增改"""
    if kwargs:
        cus_id = kwargs.get("cus_id")
        ret = models.Department.objects.filter(id=cus_id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        if kwargs:
            cus_id = kwargs.get("cus_id")
            try:
                dep_obj = Department.objects.filter(id=cus_id).update(name=name)
            except:
                return render(request, "not_found.html")
        else:
            try:
                dep_obj = Department.objects.create(name=name)
            except:
                return render(request, "not_found.html")
        return redirect("/department/")
    return render(request, "add_department.html", locals())

def delete_department(request, cus_id):
    """部门表-删除"""
    try:
        ret = Department.objects.filter(id=cus_id).delete()
    except:
        return render(request, "not_found.html")
    return redirect("/department/")


def sales(request):
    cus = Sales.objects.all()

    paginator = Paginator(cus, 10)
    current_page_num = int(request.GET.get("page", 1))
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "sales.html", locals())

def modify_sales(request, cus_id):
    """销量表-改"""

    ret = models.Sales.objects.filter(id=cus_id).first()
    if request.method == "POST":
        number = request.POST.get("number")
        try:
            dep_obj = Sales.objects.filter(id=cus_id).update(number=number)
        except:
            return render(request, "not_found.html")

        return redirect("/sales/")
    return render(request, "modify_sales.html", locals())





def aba(request, **kwargs):
    """测试用"""

    return render(request, "not_found.html")