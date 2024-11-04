from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'media')
    search_fields = ('content', 'user__username')  # Allow search by content and username
    list_filter = ('created_at',)  # Filter by creation date
    ordering = ('-created_at',)  # Order messages by newest first

admin.site.register(Message, MessageAdmin)