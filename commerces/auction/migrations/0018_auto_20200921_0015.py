# Generated by Django 3.0.8 on 2020-09-21 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0017_auto_20200919_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 21, 0, 15, 29, 68955)),
        ),
        migrations.AlterField(
            model_name='watch',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 21, 0, 15, 29, 72942)),
        ),
    ]