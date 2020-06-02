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
    name = models.CharField(verbose_name='收款人姓名', max_length=32)
    remark = models.CharField(verbose_name='备注', max_length=64)
    account_name = models.CharField(verbose_name='收款人', max_length=32)
    account_number = models.IntegerField()
    account_bank = models.CharField(verbose_name='开户银行', max_length=32)
    wechat = models.CharField(verbose_name='微信收款账号', max_length=32)

    customer = models.ForeignKey(verbose_name='所属客户', to='Customer', to_field='id', on_delete=models.CASCADE)

class Pay(models.Model):
    """支付项目表"""
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    customer = models.ForeignKey(verbose_name='客户', to='Customer', to_field='id', on_delete=models.CASCADE)
    customer_collection = models.ForeignKey(verbose_name='收款人', to='CustomerCollection', to_field='id', on_delete=models.CASCADE)

class Sales(models.Model):
    """销量表"""
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    time = models.DateTimeField(verbose_name='下单时间')

    customer = models.ForeignKey(verbose_name='所属客户', to='Customer', to_field='id', on_delete=models.CASCADE)

class Commission(models.Model):
    """提成表"""
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=12, decimal_places=3)

    sales = models.ForeignKey(verbose_name='所属客户', to='Sales', to_field='id', on_delete=models.CASCADE)

class FinishPay(models.Model):
    """已支付表"""
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(verbose_name='支付时间')
    money = models.DecimalField(max_digits=12, decimal_places=2)
    remark = models.CharField(verbose_name='备注', max_length=64)
    payment_method = models.CharField(verbose_name='支付方式', max_length=32)
    accont_number = models.IntegerField()
    account_bank = models.CharField(verbose_name='开户银行', max_length=64)

    customer = models.ForeignKey(verbose_name='客户', to='Customer', to_field='id', on_delete=models.CASCADE)
