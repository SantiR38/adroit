"""Branches views."""

# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Utilities
from adroit.branches.models import Branch
from .serializers import BranchSerializer


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

        branch = Branch.objects.all()
        serializer = BranchSerializer(branch, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BranchSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        return Response(data)