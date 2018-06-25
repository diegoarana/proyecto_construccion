from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator

class Budget(models.Models):
    consultation = models.CharField(max_length=30,  blank = False, null = False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
