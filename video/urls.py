from django.urls import path
from .views import video_list
from regis.views import group_chat
urlpatterns = [
    path('', video_list, name='video_list'),  # This will map the root URL of the app to the video_list view
]