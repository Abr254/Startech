from django.contrib import admin
from django.contrib import admin
from video.models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video')
# Register your models here.
