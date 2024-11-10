from django.contrib import admin
from .models import Post, Media, CodeSample

# Define how Post is displayed in the admin interface
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')  # Fields to display in the list view
    search_fields = ('content', 'user__username')  # Allow searching by content and user username
  # Filter posts by creation date

    # Add filtering and ordering for easier admin navigation
    ordering = ('-created_at',)

class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'file')  # Display media type, file, and date
    list_filter = ('media_type',)  # Filter by media type (image, video, etc.)
    search_fields = ('file',)  # Allow searching by file name

class CodeSampleAdmin(admin.ModelAdmin):
    list_display = ('language', 'code')  # Display language and code sample
    list_filter = ('language',)  # Filter by programming language
    search_fields = ('code',)  # Allow searching by code content

# Register the models with their respective admin configurations
admin.site.register(Post, PostAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(CodeSample, CodeSampleAdmin)