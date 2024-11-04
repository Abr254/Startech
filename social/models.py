from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import mimetypes

class Group(models.Model):
    name = models.CharField(max_length=255, default="Startech Social", unique=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)  # Text content
    media = models.FileField(upload_to='messages/media/', blank=True, null=True)  # For images/videos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"

    def clean(self):
        # Validate media type
        if self.media:
            mime_type, _ = mimetypes.guess_type(self.media.name)
            allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'video/mp4', 'video/x-msvideo']

            if mime_type not in allowed_types:
                raise ValidationError(f"Unsupported file type: {mime_type}. Only JPEG, PNG, GIF, MP4, and AVI are allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)