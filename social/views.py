from django.shortcuts import render, redirect
from .models import Group, Message
from .forms import MessageForm
import cloudinary.uploader

def get_startech_group():
    group, created = Group.objects.get_or_create(name="Startech Social")
    if created:
        print("Created new group: Startech Social")  # Optional logging
    return group

def group_chat(request):
    group = get_startech_group()  # Ensure the group exists
    messages = group.messages.all().order_by('-created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)  # Include FILES
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user

            if message.media:
                uploaded_file = request.FILES['media']  # Access the uploaded file directly

                # Check the media type before uploading
                if uploaded_file.content_type.startswith('video/'):
                    upload_result = cloudinary.uploader.upload(uploaded_file, resource_type='video')
                elif uploaded_file.content_type.startswith('image/'):
                    upload_result = cloudinary.uploader.upload(uploaded_file, resource_type='image')
                else:
                    return render(request, 'group_chat.html', {
                        'group': group,
                        'messages': messages,
                        'form': form,
                        'error': 'Unsupported file type. Please upload an image or video.'
                    })

                message.media = upload_result['secure_url']  # Save the Cloudinary URL

            message.group = group
            message.save()
            return redirect('group_chat')
    else:
        form = MessageForm()

    # Add CSS class to the media field
    form.fields['media'].widget.attrs.update({'class': 'form-control'})

    context = {
        'group': group,
        'messages': messages,
        'form': form,
    }
    return render(request, 'group_chat.html', context)

