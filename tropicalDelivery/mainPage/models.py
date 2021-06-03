from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.FloatField()
    providerId = models.IntegerField()

    def __str__(self):
        return self.title
