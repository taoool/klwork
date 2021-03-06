# Generated by Django 2.1.8 on 2020-06-02 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=3, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='客户名称')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCollection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='收款人姓名')),
                ('remark', models.CharField(max_length=64, null=True, verbose_name='备注')),
                ('account_name', models.CharField(max_length=32, null=True, verbose_name='收款人')),
                ('account_number', models.IntegerField(null=True)),
                ('account_bank', models.CharField(max_length=32, null=True, verbose_name='开户银行')),
                ('wechat', models.CharField(max_length=32, null=True, verbose_name='微信收款账号')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Customer', verbose_name='所属客户')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='FinishPay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(null=True, verbose_name='支付时间')),
                ('money', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('remark', models.CharField(max_length=64, null=True, verbose_name='备注')),
                ('payment_method', models.CharField(max_length=32, verbose_name='支付方式')),
                ('accont_number', models.IntegerField(null=True)),
                ('account_bank', models.CharField(max_length=64, null=True, verbose_name='开户银行')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Customer', verbose_name='客户')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(null=True, verbose_name='结束时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Customer', verbose_name='客户')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('time', models.DateTimeField(verbose_name='下单时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Customer', verbose_name='所属客户')),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='业务员名字')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Department', verbose_name='所属部门')),
            ],
        ),
        migrations.AddField(
            model_name='pay',
            name='saleman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='klzg.Salesman', verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='commission',
            name='sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Sales', verbose_name='所属客户'),
        ),
    ]
