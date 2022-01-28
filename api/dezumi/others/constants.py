""" Constants for general use """

from django.utils.translation import gettext_lazy as _

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
GENDER = [
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, _('Other')),
]
