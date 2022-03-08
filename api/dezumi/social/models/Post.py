""" Post related models """

from django.db import models

from dezumi.users.models import User
from dezumi.shows.models.Show import Show
from dezumi.others.models import TimeStampBase

class Post(TimeStampBase):
    """
    Post Model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True, max_length=220)
    serie = models.ForeignKey(Show, on_delete=models.CASCADE)

    total_likes = models.PositiveBigIntegerField(default=0)
    total_comments = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.content
