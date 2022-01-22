""" User related models """

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from dezumi.achievements.models.Achievement import Achievement
from dezumi.others.constants import GENDER
from dezumi.others.models import TimeStampBase

class User(AbstractUser):
    """
    Default custom user model for Dezumi API.
    """

    name = models.CharField(max_length=30)

    birth_date = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True, blank_label='Select country')
    gender = models.CharField(choices=GENDER, max_length=6, null=True, blank=True)

    total_likes = models.IntegerField(default=0)
    total_followers = models.IntegerField(default=0)
    total_friends = models.IntegerField(default=0)

    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    gins = models.IntegerField(default=0, help_text='Gin is the currency that can be used in the store.')
    featured_title = models.ForeignKey(Achievement, on_delete=models.SET_NULL, null=True, blank=True, related_name='featured_title')
    achievements = models.ManyToManyField(Achievement, through='UserAchievement', blank=True)

    is_verified = models.BooleanField(default=False, help_text='Verifies the authenticity of an account.')
    is_private = models.BooleanField(default=False, help_text='A private account only can be seen by friends.')


class UserAchievement(TimeStampBase):
    """
    Join table between User and Achievement Model
    Represents each achievement unlocked by a user
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
