from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=100)
    songid = models.CharField(max_length=20)
    artist = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    posteruri = models.CharField(max_length=2086)

    def __str__(self):
        return self.name