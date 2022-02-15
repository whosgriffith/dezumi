from django.db import models


class TimeStampBase(models.Model):
    """
    Base model for models with timestamp
    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
