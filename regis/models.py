from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# regis/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here if needed
    # e.g., profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Specify a related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Specify a related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
