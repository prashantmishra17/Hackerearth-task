from django.db import models
from django.conf import settings

class WineCollection(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=4000, null=True, blank=True)
    designation = models.TextField(max_length=4000, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    region_1 = models.CharField(max_length=100, null=True, blank=True)
    region_2 = models.CharField(max_length=100, null=True, blank=True)
    variety = models.CharField(max_length=100, null=True, blank=True)
    winery = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.description

