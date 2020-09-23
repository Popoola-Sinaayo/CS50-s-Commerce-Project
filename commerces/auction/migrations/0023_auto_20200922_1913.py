# Generated by Django 3.0.8 on 2020-09-23 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0022_auto_20200921_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='Bid_No',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 22, 19, 13, 52, 224926)),
        ),
        migrations.AlterField(
            model_name='watch',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 22, 19, 13, 52, 224926)),
        ),
    ]