from django.db import models

# Create your models here.
language = (
    ("EN", "English"),
    ("HI", "Hindi")
)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    director = models.CharField(max_length=40)
    actors = models.CharField(max_length=40)
    year = models.IntegerField()
    duration = models.IntegerField()
    language = models.CharField(choices=language, max_length=2)
    poster = models.ImageField(upload_to='media/posters')
