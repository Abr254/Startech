# regis/urls.py
from django.urls import path
from .views import register, user_login, home, user_pass # Import the home view
# regis/urls.py
from django.urls import path
from .views import register, user_login, home  # Import the home view

urlpatterns = [
    path('', home, name='home'),            # This is now the homepage
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('password-reset/', user_pass, name='pass'),  # Adjust the path as needed
]
