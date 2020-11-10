"""Products model admin."""

# Django
from django.contrib import admin

# Models
from adroit.products.models import Color, Product, Image



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

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Image model admin."""

    list_display = ('path', 'is_first', 'product_id',)