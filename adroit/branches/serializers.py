"""Branches serializers."""

# Rest Framework
from rest_framework import serializers
from rest_framework.fields import ListField

# Utilities
from .models import Branch
'''
class StringArrayField(ListField):
    """
    String representation of an array field.
    """
    def to_representation(self, obj):
        obj = super().to_representation(self, obj)
        # convert list to string
        return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
        data = data.split(",")  # convert string to list
        return super().to_internal_value(self, data)
'''
class BranchSerializer(serializers.ModelSerializer):
    """Branch model serializer."""
    state_id = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )


    class Meta:
        model = Branch
        fields = ['name', 'latitude', 'longitude', 'address', 'city', 'state', 'country', 'state_id']