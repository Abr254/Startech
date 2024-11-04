from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = CloudinaryField('video', resource_type='video')

    def __str__(self):
        return self.title
# Create your models here.
