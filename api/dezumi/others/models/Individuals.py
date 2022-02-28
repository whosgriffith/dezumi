""" User related models """

from django.db import models
from django_countries.fields import CountryField

from dezumi.others.constants import GENDER


class Person(models.Model):
    """
    Person model.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True, blank_label='Select country')
    gender = models.CharField(choices=GENDER, max_length=6, null=True, blank=True)

    total_likes = models.PositiveBigIntegerField(default=0)
    total_followers = models.PositiveBigIntegerField(default=0)
    total_favorites = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = "people"


class PersonVisual(models.Model):
    """
    Model for Person images/videos/gifs and other media.
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='visual')
    file = models.FileField(upload_to='people/visual/')

    class Meta:
        verbose_name_plural = "people visuals"


class Character(models.Model):
    """
    Character model.
    """

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    extra_info = models.FileField(upload_to='characters/extra_fields/',null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=6, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    total_likes = models.PositiveBigIntegerField(default=0)
    total_dislikes = models.PositiveBigIntegerField(default=0)
    total_favorites = models.PositiveBigIntegerField(default=0)

    likes = models.ManyToManyField('users.User', blank=True, related_name='character_likes')
    dislikes = models.ManyToManyField('users.User', blank=True, related_name='character_dislikes')
    favorites = models.ManyToManyField('users.User', blank=True, related_name='character_favorites')

    def __str__(self):
        return self.full_name


class CharacterVisual(models.Model):
    """
    Model for Character images/videos/gifs and other media.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='visual')
    file = models.FileField(upload_to='characters/visual/')

    class Meta:
        verbose_name_plural = "character visuals"
