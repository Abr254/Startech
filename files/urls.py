from django.urls import path
from files.views import upload_file, download_file, list_files

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('files/', list_files, name='list_files'),
]