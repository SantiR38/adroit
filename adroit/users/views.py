"""Users View"""

# Oauth
from oauth2_provider.views.generic import ProtectedResourceView

# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Utilities
from adroit.users.models import User

#---------- Views ----------#

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


class ListUsers(APIView):
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
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)