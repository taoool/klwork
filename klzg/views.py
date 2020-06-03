from django.shortcuts import render, redirect, HttpResponse
from klzg import models
from klzg.models import CustomerCollection, Customer, Salesman, Sales, Pay, Department, Commission, FinishPay
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

def add_customer_inf(request):
    """客户信息表-增加"""
    if request.method == "POST":
        cus = request.POST.get("customer")
        customer_obj = Customer.objects.create(name=cus)

        return redirect("/customer_inf/")

    return render(request, "add_customer_inf.html")

def modify_customer_inf(request, cus_id):
    """客户信息表-修改"""
    ret = Customer.objects.filter(id=cus_id).first()
    if request.method == "POST":
        cus = request.POST.get("customer")
        upt = Customer.objects.filter(id=cus_id).update(name=cus)
        return redirect("/customer_inf/")
    return render(request, "add_customer_inf.html", {'res': ret})

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

def add_customer(request):
    """客户收款表-增加"""
    cus = models.Customer.objects.all()
    if request.method == "POST":
        cus = request.POST.get("customer")
        a = Customer.objects.filter(name=cus).first()
        contact = request.POST.get("contact")
        remark = request.POST.get("remark")
        account = request.POST.get("account")
        account_method = request.POST.get("account_method")
        account_number = request.POST.get("account_number")
        cuscol_obj = CustomerCollection.objects.create(name=contact, remark=remark, account_name=account, account_method=account_method, account_number=account_number, customer_id=a.id)
        return redirect("/customer/")

    return render(request, "add_customer.html", {"cus": cus})

def modify_customer(request, cus_id):
    """客户收款表-修改"""
    ret = CustomerCollection.objects.filter(id=cus_id).first()
    cus = models.Customer.objects.all()
    if request.method == "POST":
        cus = request.POST.get("customer")
        a = Customer.objects.filter(name=cus).first()
        contact = request.POST.get("contact")
        remark = request.POST.get("remark")
        account = request.POST.get("account")
        account_method = request.POST.get("account_method")
        account_number = request.POST.get("account_number")
        cuscol_obj = CustomerCollection.objects.filter(id=cus_id).update(name=contact, remark=remark, account_name=account, account_method=account_method, account_number=account_number,customer=a.id)
        return redirect("/customer/")
    return render(request, "add_customer.html", {'ret': ret, "cus": cus})

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

def add_salesman(request):
    """业务员信息-增加"""
    cus = models.Department.objects.all()
    if request.method == "POST":
        name = request.POST.get("salesman")
        department = request.POST.get("department")
        a = Department.objects.filter(name=department).first()
        sal_obj = Salesman.objects.create(name=name, department_id=a.id)
        return redirect("/salesman/")
    return render(request, "add_salesman.html", {'cus': cus})

def modify_salesman(request, cus_id):
    """业务员信息-修改"""
    cus = models.Department.objects.all()
    ret = models.Salesman.objects.filter(id=cus_id).first()
    if request.method == "POST":
        name = request.POST.get("salesman")
        department = request.POST.get("department")
        a = Department.objects.filter(name=department).first()
        sal_obj = Salesman.objects.filter(id=cus_id).update(name=name, department_id=a.id)
        return redirect("/salesman/")
    return render(request, "add_salesman.html", {"cus": cus, "ret": ret})

def delete_salesman(request, cus_id):
    """业务员信息-删除"""
    sal_obj = Salesman.objects.filter(id=cus_id).delete()
    return redirect("/salesman/")


def project(request):
    """项目表"""
    ret = models.Pay.objects.all()
    if request.method == "POST":
        sea = request.POST.get("cust")
        ret = models.Pay.objects.filter(customer__name__contains=sea).all()
    return render(request, "project.html", {"ret": ret})

def add_project(request):
    if request.method == "POST":
        pass
    return render(request, "add_project.html")


def modify_project(request):
    pass

def delete_project(request):
    pass

def pay(request):
    """提成表"""
    ret = models.Commission.objects.all()
    return render(request, "pay.html", {"ret": ret})

def add_pay(request):
    pass

def modify_pay(request):
    pass

def delete_pay(request):
    pass

def finish(request):
    """付款记录表"""
    ret = models.FinishPay.objects.all()
    return render(request, "finish.html", {"ret": ret})

def add_finish(request):
    pass

def modify_finish(request):
    pass

def delete_finish(request):
    pass

def department(request):
    """部门表"""
    ret = models.Department.objects.all()
    if request.method == "POST":
        sea = request.POST.get("search")
        ret = models.Department.objects.filter(name__contains=sea).all()
    return render(request, "department.html", {"ret": ret})

def add_department(request):
    """部门表-增加"""
    if request.method == "POST":
        name = request.POST.get("name")
        dep_obj = Department.objects.create(name=name)
        return redirect("/department/")
    return render(request, "add_department.html")

def modify_department(request, cus_id):
    """部门表-修改"""
    ret = models.Department.objects.filter(id=cus_id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        dep_obj = Department.objects.filter(id=cus_id).update(name=name)
        return redirect("/department/")
    return render(request, "add_department.html", {"ret": ret})

def delete_department(request, cus_id):
    """部门表-删除"""
    ret = Department.objects.filter(id=cus_id).delete()
    return redirect("/department/")







def aba(request):
    """测试用"""
    return render(request, "add_customer.html")