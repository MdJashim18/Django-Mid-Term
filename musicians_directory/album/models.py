from django.db import models
from musician.models import MusicianModel


class AlbumModel(models.Model):
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE, related_name='albums')
    album_name = models.CharField(max_length=20)
    release_date = models.DateField() 
    RATING_CHOICES = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    ]
    rating = models.CharField(choices=RATING_CHOICES, max_length=1)
