"""Sendings admin."""

# Django
from django.contrib import admin

# Utilities
from adroit.sendings.models import Sending

@admin.register(Sending)
class SendingAdmin(admin.ModelAdmin):
    """Sending model admin."""

    list_display = ('user_id', 
                    'invoice_id',
                    'latitude',
                    'longitude',
                    'branch_id',
                    'distance',
                    'going_time',
                    'arrival_time',
                    'state_id',)

    search_fields = ('user_id__first_name', 
                     'user_id__last_name',
                     'branch_id',
                     "branch_id__city",
                     "branch_id__state",
                     "branch_id__country")

    list_filter = ('created',
                   'modified',
                   'branch_id__code',
                   "branch_id__city",
                   "branch_id__state",
                   "branch_id__country")
