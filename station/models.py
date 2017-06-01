from django.db import models

# Create your models here.
class Reading(models.Model):
    location = models.CharField(max_length=100)
    weather = models.CharField(max_length=20)
    temp = models.IntegerField()
    humidity = models.CharField(default='None', max_length=10)
    icon_url = models.URLField(default='None')
    observation_time = models.CharField(default='None', max_length=100)
