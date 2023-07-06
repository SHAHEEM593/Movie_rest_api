from django.db import models

class Movie(models.Model):
    moviename = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    released = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.moviename
