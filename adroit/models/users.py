"""User models."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

# Utilities
from utils.models import AdroitModel

class User(AdroitModel, AbstractUser):
    """ User models.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email adress',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d(9,15)$',
        message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username