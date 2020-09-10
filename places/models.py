from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=400)
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=19, decimal_places=16)
    lat = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return f"{self.title}"
