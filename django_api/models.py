# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()

