""" Django models utilities """

#Django
from django.db import models

class AdroitModel(models.Model):
    """Adroit Base model.

    AdroitModel acts as an abstract base class from wich every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        +modified (DateTime): Store the last datetime the object was modified.
    """

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