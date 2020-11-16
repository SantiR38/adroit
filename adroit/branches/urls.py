"""Branches urls"""

# Django
from django.urls import path

# Utilities
from .views import ListBranches


urlpatterns = [

    path('list_branches/', ListBranches.as_view()),

]