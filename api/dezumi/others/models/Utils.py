from django.db import models


class BaseModel(models.Model):
    """
    Base model
    With timestamp
    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
