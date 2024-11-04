from django.urls import path
from .views import video_list
urlpatterns = [
    path('', video_list, name='video_list'),  # This will map the root URL of the app to the video_list view
]