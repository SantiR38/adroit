""" Django models utilities """

# Django
from django.db import models

class AdroitModel(models.Model):
    """Adroit Base model.

    AdroitModel acts as an abstract base class from wich every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """
    code = models.CharField(max_length=20, unique=True, blank=True)
    state_id = models.ManyToManyField('utils.State')
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option"""

        abstract = True # This means that has not be migrated as a table in the database
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class State(models.Model):
    """State model.

    This model contains all the states of every product, sale, branch, etc.
    The abstract class AdroitModel is linked with these by many-to-many field(state_id field).
    Necesary states:
        + Active
        + Inactive
        + Deleted
        + Featured
        + Best Seller
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

