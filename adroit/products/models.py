"""Products models."""

# Django
from django.db import models

# Utilities
from adroit.utils.models import AdroitModel


class Product(AdroitModel):
    """Product model.

    If the same product is in two or more different branches, the code is going to have some variations.
    E.g. 883424-a for branch a
         883424-b for branch b
    """

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    profit_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descount_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    section = models.CharField(max_length=100, blank=True) # blank=True hace que el valor vacio no se guarde como None, sino como ''.
    brand = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    state_id = models.ForeignKey('utils.State', on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField(verbose_name="Cantidad")
    stock_alarm = models.IntegerField(verbose_name="Stock minimo permitido", null=True)
    branch_id = models.ForeignKey('branches.Branch', on_delete=models.SET_NULL, null=True)


class Color(AdroitModel):
    """Color model.

    Every product is going to have featured colors.
    These are going to be saved with an hexadecimal 
    code, and are going to have a one-to-many 
    relationship with Product model.
    """

    code = models.CharField(max_length=20)
    avaliable = models.BooleanField(default=False)
    product_id = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)

class Image(AdroitModel):
    """Image model.

    Every product is going to have at least one image to show,
    and only one is going to be featured.
    These are in '/media' directory, so we need a url field to search it. 
    """

    path = models.URLField()
    is_first = models.BooleanField(default=False)
    product_id = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)