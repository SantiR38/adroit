"""Branches models."""

# Django
from django.db import models

# Utilities
from adroit.utils.models import AdroitModel


class Branch(AdroitModel):
    """Branch model.
    
    With this model, you can specify in the code or in
    a foreing key where belongs some product.
    
    Also, you can create an entire system for a specific branch,
    with employees and delivery management.
    """

    name = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    adress = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Branches'