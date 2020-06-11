from django.db import models

# Create your models here.
class Salesman(models.Model):
    """业务员信息表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='业务员名字', max_length=32)

    department = models.ForeignKey(verbose_name='所属部门', to='Department', to_field='id', on_delete=models.CASCADE)

class Department(models.Model):
    """部门表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='部门名称', max_length=32)

class Customer(models.Model):
    """客户表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='客户名称', max_length=100)

class CustomerCollection(models.Model):
    """客户收款人信息表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='联络人', max_length=32)
    remark = models.CharField(verbose_name='备注', max_length=64, null=True, default='无')
    account_name = models.CharField(verbose_name='收款人', max_length=32, null=True)
    account_number = models.BigIntegerField(null=True)
    account_method = models.CharField(verbose_name='收款方式', max_length=32, null=True)


    customer = models.ForeignKey(verbose_name='所属客户', to='Customer', to_field='id', on_delete=models.CASCADE)

class Pay(models.Model):
    """支付项目表"""
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间', null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


    customercol = models.ForeignKey(verbose_name='客户联络人', to='CustomerCollection', to_field='id', on_delete=models.CASCADE)
    salesman = models.ForeignKey(verbose_name='业务负责人', to='Salesman', to_field='id', on_delete=models.CASCADE, null=True)

class Commission(models.Model):
    """提成表"""
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=12, decimal_places=3)
    money = models.DecimalField(verbose_name="已付", max_digits=12, decimal_places=3, default=0)

    pay = models.ForeignKey(verbose_name='订单号', to='Pay', to_field='id', on_delete=models.CASCADE)
    sales = models.ForeignKey(verbose_name='销量', to='Sales', to_field='id', on_delete=models.CASCADE)

class FinishPay(models.Model):
    """已支付表"""
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(verbose_name='支付时间', null=True)
    money = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    remark = models.CharField(verbose_name='备注', max_length=64, null=True, default='无')
    payment_method = models.CharField(verbose_name='支付方式', max_length=32)
    account_number = models.IntegerField(null=True)

    customercol = models.ForeignKey(verbose_name='客户联络人', to='CustomerCollection', to_field='id', on_delete=models.CASCADE)

class Sales(models.Model):
    """销量表"""
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(verbose_name="月销量", null=True)
    number = models.IntegerField(null=True)

class History(models.Model):
    """导入记录"""
    id = models.AutoField(primary_key=True)
    salesman = models.CharField(verbose_name="业务员", max_length=32)
    time = models.DateTimeField(verbose_name="时间", null=True)
    customer = models.CharField(verbose_name="客户", max_length=64)
    customercol = models.CharField(verbose_name="联络人", max_length=32)
    number = models.IntegerField(verbose_name="销量")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
