# Generated by Django 3.1.7 on 2021-06-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0008_cart_costumerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CostumerID', models.CharField(max_length=200)),
                ('CartID', models.CharField(max_length=200)),
                ('isOngoing', models.CharField(default='', max_length=200)),
                ('DeliveryArea', models.FloatField()),
                ('time', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
