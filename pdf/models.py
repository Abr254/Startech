# models.py
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()  # Text content of the post
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Media (can be image or video)
    media = models.ManyToManyField('Media', blank=True)

    # Code Sample
    code_sample = models.ForeignKey('CodeSample', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

class Media(models.Model):
    IMAGE = 'image'
    VIDEO = 'video'
    
    MEDIA_TYPES = [(IMAGE, 'Image'), (VIDEO, 'Video')]
    
    file = CloudinaryField('file')
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    
    def __str__(self):
        return f"{self.media_type} file"

class CodeSample(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=100)

    def __str__(self):
        return f"Code Sample ({self.language})"