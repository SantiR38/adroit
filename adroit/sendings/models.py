"""Sendings models."""

#Django
from django.db import models

# Utilities
from adroit.utils.models import AdroitModel


class Sending(AdroitModel):
    """Sending model.
    
    This model is going to register delivery details.

    It will be referenced in Invoice model as
    a one to one field. 
    """

    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    invoice_id = models.ForeignKey('sales.Invoice', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    branch_id = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    distance = models.CharField(max_length=25)
    going_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True)
    state_id = models.ForeignKey('utils.State', on_delete=models.SET_NULL, null=True)