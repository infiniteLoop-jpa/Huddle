from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from .models import Account, HuddleGroup
from django.http import JsonResponse

def huddle_home(request):
    # Get user information from the session
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    if not user_id or not username:
        # If user information is not in the session, redirect to login
        return redirect('Huddle_app:huddle_login')

    try:
        # Get the user's account
        account = Account.objects.get(id=user_id, username=username)

        # Get the user's huddle groups
        huddle_groups = HuddleGroup.objects.filter(members=account)

        return render(request, 'index.html', {'account': account, 'huddle_groups': huddle_groups})
    except Account.DoesNotExist:
        # If the user does not exist, display an error message
        messages.error(request, "User not found.")
        return redirect('Huddle_app:huddle_login')

def create_huddle(request):
    if request.method == 'POST':
        # Assuming you have a form with 'huddleName' and 'members' fields
        huddle_name = request.POST.get('huddleName')
        members_emails = request.POST.get('members')

        # Get user information from the session
        user_id = request.session.get('user_id')
        username = request.session.get('username')

        if not user_id or not username:
            # If user information is not in the session, redirect to login
            return JsonResponse({'success': False, 'error': 'User not authenticated.'})

        # Get the user's account
        account = Account.objects.get(username=username)

        # Create a new HuddleGroup instance and save it to the database
        huddle_group = HuddleGroup.objects.create(
            name=huddle_name,
            members=members_emails,
        )

        # Add the new huddle group to the user's groups
        account.groups.add(huddle_group)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

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
                # Set user information in the session
                request.session['user_id'] = user.id
                request.session['username'] = user.username

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
