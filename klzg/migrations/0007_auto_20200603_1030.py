# Generated by Django 2.1.8 on 2020-06-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klzg', '0006_auto_20200603_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercollection',
            name='remark',
            field=models.CharField(default='无', max_length=64, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='finishpay',
            name='remark',
            field=models.CharField(default='无', max_length=64, null=True, verbose_name='备注'),
        ),
    ]
