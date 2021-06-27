from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='doc')
    song = models.FileField(upload_to='doc')
    movie = models.CharField(max_length=2000)
    lyrics = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.name
