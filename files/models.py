from django.db import models
from .storage import CloudinaryStorage
from django.db import models
from .storage import CloudinaryStorage

class Document(models.Model):
    file = models.FileField(upload_to='documents/', storage=CloudinaryStorage)
    title = models.CharField(max_length=255)  # New field for title
    description = models.TextField(blank=True)  # New field for description
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

# Create your models here.
