from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    album_ratings = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.album_name
    