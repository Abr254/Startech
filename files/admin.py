from django.contrib import admin
from django.contrib import admin
from files.models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('file',)

admin.site.register(Document, DocumentAdmin)
# Register your models here.
