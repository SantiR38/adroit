"""Profile models."""

# Django
from django.db import models

# Utilities
from .users import User


class Profile(models.Model):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statistics.
    """
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)