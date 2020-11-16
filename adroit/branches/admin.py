"""Branches models admin."""

# Django
from django.contrib import admin

# Utilities
from adroit.branches.models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    """Branch model admin."""

    list_display = ('code', 'name', 'latitude', 'longitude', 'address', 'city', 'state', 'country',)
    search_fields = ('name', 'latitude', 'longitude', 'adress', 'city', 'state', 'country',)
    list_filter = ('state', 'country',)

