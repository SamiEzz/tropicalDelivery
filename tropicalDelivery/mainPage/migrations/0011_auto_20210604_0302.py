# Generated by Django 3.1.7 on 2021-06-04 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0010_auto_20210604_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='DeliveryArea',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(blank=True, default='', null=True),
        ),
    ]
