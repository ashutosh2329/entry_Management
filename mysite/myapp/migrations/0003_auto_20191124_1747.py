# Generated by Django 2.2.7 on 2019-11-24 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191124_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 24, 17, 47, 20, 230375), verbose_name='time arrived'),
        ),
    ]
