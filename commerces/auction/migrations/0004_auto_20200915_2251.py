# Generated by Django 3.0.8 on 2020-09-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20200915_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bids',
            name='Start_Bid',
            field=models.IntegerField(),
        ),
    ]