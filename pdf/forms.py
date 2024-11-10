from django import forms
from .models import Post, Media, CodeSample

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Assuming content is the only field for a post

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['media_type', 'file']  # Assuming media has a 'file' field for the uploaded media

class CodeSampleForm(forms.ModelForm):
    class Meta:
        model = CodeSample
        fields = ['code', 'language']  # Fields for the code sample (e.g., code text and programming language)