from django.shortcuts import render
from django.shortcuts import render, redirect
from files.forms import DocumentForm
from files.models import Document
import cloudinary
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')  # Redirect after upload
    else:
        form = DocumentForm()
    
    documents = Document.objects.all()  # Get all documents for display
    return render(request, 'upload.html', {'form': form, 'documents': documents})
    
def download_file(request, file_id):
    document = Document.objects.get(id=file_id)
    url = document.file.url
    return redirect(url)

def list_files(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})
# Create your views here.
