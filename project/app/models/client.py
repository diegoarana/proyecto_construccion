from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator

class Client (models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=30, blank=False, null=False)
    location = models.CharField(max_length=30, blank=False, null=False)
    phone = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(999999999999999)], blank=False, null=False)

    def __str__(self):
        return self.email