# views.py
from django.shortcuts import render, redirect
from .forms import PostForm, MediaForm, CodeSampleForm
from .models import Post, Media, CodeSample

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'pdf_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        media_form = MediaForm(request.POST, request.FILES)
        code_form = CodeSampleForm(request.POST)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            # Handle media upload
            if media_form.is_valid():
                media_instance = media_form.save()
                post.media.add(media_instance)
            
            # Handle code sample submission
            if code_form.is_valid():
                code_sample = code_form.save()
                post.code_sample = code_sample
            
            post.save()
            return redirect('home')

    else:
        post_form = PostForm()
        media_form = MediaForm()
        code_form = CodeSampleForm()

    return render(request, 'upload_pdf.html', {
        'post_form': post_form,
        'media_form': media_form,
        'code_form': code_form,
    })