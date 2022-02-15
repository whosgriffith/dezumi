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

    total_likes = models.IntegerField(default=0)
    total_followers = models.IntegerField(default=0)
    total_favorites = models.IntegerField(default=0)

    # 'user.User' instead of import User because of cirular import error (More: https://stackoverflow.com/a/4379094)
    follows = models.ManyToManyField('users.User', blank=True, related_name='person_follows')
    likes = models.ManyToManyField('users.User', blank=True, related_name='person_likes')
    favorites = models.ManyToManyField('users.User', blank=True, related_name='person_favorites')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = "people"


class PersonMedia(models.Model):
    """
    Model for Person media.
    """
    file = models.FileField(upload_to='people')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='media')

    class Meta:
        verbose_name_plural = "people media"
    