# Generated by Django 3.0.8 on 2020-09-16 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_auto_20200916_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Image',
            field=models.ImageField(default='/static/auction/img/icon-3.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 16, 1, 49, 35, 720455)),
        ),
    ]