"""User model admin."""

# Django
from django.contrib import admin

# Models
from adroit.utils.models import State



@admin.register(State)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('name',)
