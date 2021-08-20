from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
     # author, title, content
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=500, null = True)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Workout(models.Model):
    #link, created by, details
    user = models.CharField(max_length=50, null = True)
    instructor = models.CharField(max_length=50)
    title = models.CharField(max_length=500, null = True)
    url = models.URLField(max_length=200)
    details = models.TextField()


class Recipe(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=500, null = True)
    details = models.TextField()
    photo = models.ImageField()









