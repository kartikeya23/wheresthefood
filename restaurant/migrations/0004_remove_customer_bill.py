# Generated by Django 3.0.2 on 2020-01-20 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200119_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='bill',
        ),
    ]
