# Generated by Django 3.1.7 on 2021-06-04 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0020_auto_20210604_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='providerId',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainPage.provider'),
        ),
    ]
