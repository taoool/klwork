# Generated by Django 2.1.8 on 2020-06-16 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0003_auto_20200615_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 17, 9, 53, 703415), verbose_name='导入时间'),
        ),
    ]
