# Generated by Django 3.0.8 on 2020-09-16 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_listing_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Image',
            field=models.ImageField(default='C: / Users/HP/commerces/auction/static/auction/img/icon-3.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 16, 1, 6, 28, 765495)),
        ),
    ]
