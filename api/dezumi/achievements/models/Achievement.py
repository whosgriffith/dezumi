""" Achievements related models """

from django.db import models


class Achievement(models.Model):
    """
    Achievements Model
    """

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    badge = models.ImageField(upload_to='achievements/badges/', blank=True, null=True)

    def __str__(self):
        return self.title
