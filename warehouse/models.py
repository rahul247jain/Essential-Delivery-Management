from django.db import models
from shop.models import Product

# Create your models here.


class Warehouse(models.Model):
    location = models.CharField(max_length=50)
    loc_x = models.DecimalField(max_digits=10, decimal_places=6)
    loc_y = models.DecimalField(max_digits=10, decimal_places=6)


class KeyVal(models.Model):
    locname = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
