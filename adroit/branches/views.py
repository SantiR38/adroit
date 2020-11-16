"""Branches views."""

# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Utilities
from adroit.branches.models import Branch


#---------- Views ----------#

class ListBranches(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        branches = {}
        i = 1
        for branch in Branch.objects.all():
            branches['branch'+str(i)] = {
                'code': branch.code,
                'state_id': branch.state_id.name,
                'latitude': branch.latitude,
                'longitude': branch.longitude,
                'longitude': branch.longitude,
                'address': branch.address,
                'city': branch.city,
                'state': branch.state,
                'country': branch.country
            }
            i += 1
        return Response(branches)
