# Generated by Django 3.1.7 on 2021-06-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
