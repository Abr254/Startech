from django.urls import path
from .views import group_chat
urlpatterns = [
    path('group/', group_chat, name='group_chat'),  # Only one group chat view
]