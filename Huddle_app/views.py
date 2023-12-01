from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account
from django.contrib import messages
# Create your views here.

def huddle_home(request):
    return render(request, 'index.html')

def huddle_group(request):
    return render(request, 'huddle_page.html')

def huddle_login(request):
    return render(request, 'login.html')

def huddle_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('Huddle_app:huddle_signup')

        # Assuming you have a simple Account model
        account = Account(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1  # Store the password securely using Django's password hashing
        )

        account.save()

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('Huddle_app:huddle_login')

    return render(request, 'signup.html')