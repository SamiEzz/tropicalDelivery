# Generated by Django 3.1.7 on 2021-06-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('openinghours', models.CharField(max_length=200)),
            ],
        ),
    ]
