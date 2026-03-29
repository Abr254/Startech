# urls.py
from django.urls import path
from . import views
#rom regis.views import group_chat

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('',views.member,name='member'),
]