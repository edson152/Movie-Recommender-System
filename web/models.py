from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Movie(models.Model):
    objects = None
    objects = None
    objects = None
    objects = None
    title   	= models.CharField(max_length=200)
    genre  		= models.CharField(max_length=100)
    movie_logo  = models.FileField()

    def __str__(self):
        return self.title

class Myrating(models.Model):
    objects = None
    user   	= models.ForeignKey(User,on_delete=models.CASCADE)
    movie 	= models.ForeignKey(Movie,on_delete=models.CASCADE)
    rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
