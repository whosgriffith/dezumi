""" Constants related to shows """

from django.utils.translation import gettext_lazy as _

SERIE = '0'
MOVIE = '1'
OVA = '2'
ONA = '3'
SHOW_TYPES = [
    (SERIE, _('Serie')),
    (MOVIE, _('Movie')),
    (OVA, _('OVA')),
    (ONA, _('ONA')),
]