"""Products model admin."""

# Django
from django.contrib import admin

# Models
from adroit.products.models import Color, Product



@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """Color model admin."""

    list_display = ('code', 'avaliable', 'product_id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product model admin."""

    list_display = ('code', 'name', 'cost', 'profit_percent',
                    'precio', 'descount_percent', 'section',
                    'brand', 'stock', 'stock_alarm',)