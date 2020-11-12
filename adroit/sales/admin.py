"""Sales model admin."""

# Django
from django.contrib import admin

# Utilities
from adroit.sales.models import Invoice, InvoiceDetail

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """Invoice model admin."""

    list_display = ('state_id', 
                    'payment_method',
                    'subtotal', 'discount',
                    'total_discounted',
                    'total',
                    'branch_id',)

    search_fields = ('state_id', 
                     'payment_method',
                     'total', 'branch_id',
                     "branch_id__city",
                     "branch_id__state",
                     "branch_id__country")

    list_filter = ('created', 'modified', 
                   'payment_method',
                   'branch_id__code',
                   "branch_id__city",
                   "branch_id__state",
                   "branch_id__country")

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    """InvoiceDetail model admin."""

    list_display = ('invoice_id', 
                    'unit_cost',
                    'unit_price',
                    'discount',
                    'quantity',
                    'product_id',)

    search_fields = ('invoice_id',
                     "product_id__name",)

    list_filter = ('created',
                   'modified',)