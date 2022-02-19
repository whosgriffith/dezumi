""" User related models """

from django.db import models
from django.utils.translation import gettext_lazy as _

# ANNOUNCED = 0
# UPCOMING = 1
# FINISHED = 2
# SHOW_STATUS = [
#     (ANNOUNCED, _('Announced')),
#     (UPCOMING, _('Upcoming')),
#     (FINISHED, _('Finished')),
# ]



class ShowType(models.Model):
    """
    Model for Show types.
    """
    type = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "show types"


class ShowVisual(models.Model):
    """
    Model for Show images/videos/gifs and other media.
    """
    file = models.FileField(upload_to='shows/visual/')

    class Meta:
        verbose_name_plural = "shows visuals"


class Studio(models.Model):
    """
    Studio model (for Anime/Movies and others)
    """

    name = models.CharField(max_length=60)
    established = models.DateTimeField(null=True, blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to='studio/visuals/')


class Show(models.Model):
    """
    Show model (for Anime/Movies and others)
    """

    title = models.CharField(max_length=60)
    key_art = models.ForeignKey(ShowVisual, on_delete=models.SET_NULL, null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    airing = models.BooleanField(default=False)
    season = models.PositiveIntegerField(default=0)
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True, blank=True)
    #producer = models.ForeignKey(Producer)
    release_date = models.DateField(null=True, blank=True)
    episodes = models.PositiveIntegerField(default=0)
    duration = models.PositiveIntegerField(default=0)
    show_type = models.ForeignKey(ShowType, on_delete=models.SET_NULL, null=True, blank=True)

    visuals = models.ManyToManyField(ShowVisual, related_name="visuals")

    total_likes = models.PositiveBigIntegerField(default=0)
    total_favorites = models.PositiveBigIntegerField(default=0)
    total_completed = models.PositiveBigIntegerField(default=0)
    total_watching = models.PositiveBigIntegerField(default=0)
    total_dropped = models.PositiveBigIntegerField(default=0)
    total_plan = models.PositiveBigIntegerField(default=0)
    total_reviews = models.PositiveBigIntegerField(default=0)
    total_recommended = models.PositiveBigIntegerField(default=0)
    total_not_recommended = models.PositiveBigIntegerField(default=0)

    dezumi_score = models.FloatField(default=0)
