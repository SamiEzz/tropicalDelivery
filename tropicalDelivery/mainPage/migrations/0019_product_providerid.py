# Generated by Django 3.1.7 on 2021-06-04 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0018_remove_product_providerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='providerId',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
