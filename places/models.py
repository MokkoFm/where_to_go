from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description_short = models.TextField(
        null=True, blank=True, verbose_name="Short description")
    description_long = HTMLField(
        null=True, blank=True, verbose_name="Long description")
    lng = models.FloatField(verbose_name="Longitude")
    lat = models.FloatField(verbose_name="Latitude")

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField(
        upload_to="places", verbose_name="Picture")
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name="images",
                              verbose_name="Place of picture")
    position = models.PositiveIntegerField(
        blank=True, default=0, verbose_name="Number of picture")

    def __str__(self):
        return f"{self.position} {self.place}"

    class Meta(object):
        ordering = ['position']
