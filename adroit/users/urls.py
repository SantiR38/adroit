"""Users urls"""

# Django
from django.urls import path

# Utilities
from . import views
from .views import ApiEndpoint, ListUsers


urlpatterns = [

    path('secret/', views.secret_page, name='secret'),
    path('hello/', ApiEndpoint.as_view()),
    path('list_users/', ListUsers.as_view()),

]