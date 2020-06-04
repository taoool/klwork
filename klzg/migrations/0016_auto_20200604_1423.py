# Generated by Django 2.1.8 on 2020-06-04 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klzg', '0015_auto_20200604_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klzg.Pay', verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='number',
            field=models.IntegerField(),
        ),
    ]
