# Generated by Django 2.1.8 on 2020-06-04 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klzg', '0019_auto_20200604_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finishpay',
            old_name='accont_number',
            new_name='account_number',
        ),
    ]