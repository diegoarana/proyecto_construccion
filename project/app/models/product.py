from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator

class Product(models.Model):

    PRODUCT_TYPES = (
        (0, 'Producto'),
        (1, 'Obra realizada')
    )

    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=30, blank=False, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    product_type = models.IntegerField(null=False, choices=PRODUCT_TYPES, null=False)
    image = models.ImageField(upload_to='products')