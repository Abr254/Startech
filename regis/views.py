# regis/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from regis.forms import UserRegisterForm, UserLoginForm

def home(request):
    return render(request, 'home.html')  # Ensure 'home.html' is in your templates directory

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})  # Ensure 'form' is passed correctly
def user_pass(request):
    if request.method == 'POST':
        # Handle form submission logic here (e.g., validate and send password reset email)
        pass  # Replace with actual logic
    return render(request, 'pass.html')
    
def user_login(request):
    form = UserLoginForm()  # Initialize the form outside the POST condition
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Use the POST data to populate the form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('group_chat')  # Redirect to the social page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission. Please check your input.')

    return render(request, 'login.html', {'form': form})  # Pass the form to the template