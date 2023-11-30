from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    musician = models.CharField(max_length=100)
    image = models.ImageField(upload_to="music_image")
    date = models.DateTimeField(auto_now_add=True)
    music_file = models.FileField(upload_to="music")

    def __str__(self):
        return self.title
