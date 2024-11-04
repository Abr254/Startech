from django.shortcuts import render
from django.shortcuts import render
from video.models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
# Create your views here.
