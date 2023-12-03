from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from .models import Account, HuddleGroup

def huddle_home(request):
    # Get the user from the request
    user = request.user if request.user.is_authenticated else None

    if not user:
        return redirect('Huddle_app:huddle_login')

    # Get the user's account
    account = Account.objects.get(username=user.username)

    # Get the user's huddle groups
    huddle_groups = HuddleGroup.objects.filter(members=account)

    return render(request, 'index.html', {'account': account, 'huddle_groups': huddle_groups})

def huddle_group(request):
    return render(request, 'huddle_page.html')

def huddle_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Try to get the user from the database
            user = Account.objects.get(username=username)
            
            # Check if the provided password matches
            if password == user.password:
                return redirect('Huddle_app:huddle_home')  # Redirect to the home page after login
            else:
                # If the password is not valid, display an error message
                messages.error(request, "Invalid username or password.")
                return redirect('Huddle_app:huddle_login')
        except Account.DoesNotExist:
            # If the user does not exist, display an error message
            messages.error(request, "Invalid username or password.")
            return redirect('Huddle_app:huddle_login')

    return render(request, 'login.html')

def huddle_signup(request):
    if request.method == 'POST':
        # Extract data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Perform basic form validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('Huddle_app:huddle_signup')

        # Check if the username or email is already taken
        if Account.objects.filter(username=username).exists() or Account.objects.filter(email=email).exists():
            messages.error(request, "Username or email already taken.")
            return redirect('Huddle_app:huddle_signup')

        # Create an Account instance and save it to the database
        account = Account(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1
        )
        account.save()

        # Optionally, you might want to log in the user after signing up
        # For simplicity, we'll redirect to the login page
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('Huddle_app:huddle_login')

    return render(request, 'signup.html')
