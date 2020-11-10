"""Products model admin."""

# Django
from django.contrib import admin

# Models
from adroit.products.models import Color



@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """Color model admin."""

    list_display = ('code', 'avaliable', 'product_id',)
