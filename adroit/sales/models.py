"""Sales models."""

# Django
from django.db import models

# Utilities
from adroit.utils.models import AdroitModel


class Invoice(AdroitModel):
    """Invoice model.
    
    This model is going to register specifics sales.

    It will be referenced in InvoiceDetail model as
    a foreign key. 
    """

    state_id = models.ForeignKey('utils.state', on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=50, default="Cash") # In the forms is going to be an option field
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_discounted = models.DecimalField(max_digits=10, decimal_places=2)
    # sending_id: one to one(Sending)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    #client_id = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    #seller_id = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    branch_id = models.ForeignKey('branches.Branch', on_delete=models.SET_NULL, null=True)