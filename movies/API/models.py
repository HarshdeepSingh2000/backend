
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)

class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uuid = models.UUIDField(unique=True)
    movies = models.ManyToManyField(Movie, related_name='collections')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional user-related fields if needed
