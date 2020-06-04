# Generated by Django 2.1.8 on 2020-06-03 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klzg', '0004_remove_finishpay_account_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='time',
        ),
        migrations.AddField(
            model_name='sales',
            name='pay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='klzg.Pay', verbose_name='支付项目'),
        ),
    ]