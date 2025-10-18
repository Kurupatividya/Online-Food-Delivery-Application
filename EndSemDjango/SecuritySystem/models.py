from django.db import models


# Create your models here.
class MEMBERSHIP(models.Model):
    thumbnails = models.CharField(max_length=60)
    price = models.IntegerField()
    qty = models.CharField(max_length=100)
