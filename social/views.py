from django.shortcuts import render, redirect
from .models import Group, Message
from .forms import MessageForm
import cloudinary.uploader

def get_startech_group():
    # Ensure the "Startech Social" group exists, creating it if necessary
    group, created = Group.objects.get_or_create(name="Startech Social")
    if created:
        print("Created new group: Startech Social")  # Optional logging
    return group

def group_chat(request):
    group = get_startech_group()  # Ensure the group exists
    messages = group.messages.all().order_by('-created_at')

    # Determine media type for each message (video or image)
    for message in messages:
        if message.media:
            # Access the file name (or URL) and check the extension
            if message.media.name.endswith('.mp4') or message.media.name.endswith('.mov'):
                message.is_video = True
            else:
                message.is_video = False
        else:
            message.is_video = False

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)  # Include FILES for media upload
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user  # Assign the user who sent the message

            if message.media:
                uploaded_file = request.FILES['media']  # Access the uploaded file directly

                # Check the media type before uploading to Cloudinary
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

                # Store the Cloudinary URL of the uploaded media
                message.media = upload_result['secure_url']

            message.group = group
            message.save()  # Save the message in the database
            return redirect('group_chat')  # Redirect to the same page to refresh the messages
    else:
        form = MessageForm()  # Initialize an empty form for GET request

    # Add CSS class to the media field
    form.fields['media'].widget.attrs.update({'class': 'form-control'})

    context = {
        'group': group,
        'messages': messages,
        'form': form,
    }
    return render(request, 'group_chat.html', context)