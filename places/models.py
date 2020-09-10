from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=400, null=True, blank=True)
    description_long = models.TextField(null=True, blank=True)
    lng = models.DecimalField(max_digits=19, decimal_places=16)
    lat = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="places", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
