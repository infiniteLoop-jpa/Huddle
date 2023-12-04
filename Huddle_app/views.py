from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.contrib import messages
from .models import Account, HuddleGroup, Task
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect



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
        members_emails = members_emails + ', ' + account.email
        # Create a new HuddleGroup instance and save it to the database
        huddle_group = HuddleGroup.objects.create(
            name=huddle_name,
        )
        # Use set() to add members to the many-to-many relationship
        huddle_group.members.set(Account.objects.filter(email__in=members_emails.replace(' ', '').split(',')))

        # Fetch the user's huddle groups
        huddle_groups = HuddleGroup.objects.filter(members=account)

        # Pass the user's huddle groups to the template
        return redirect('Huddle_app:huddle_home')

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def huddle_group(request, huddle_group_id):
    # Get user information from the session
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    if not user_id or not username:
        # If user information is not in the session, redirect to login
        return redirect('Huddle_app:huddle_login')

    try:
        # Get the user's huddle groups
        huddle_group = get_object_or_404(HuddleGroup, id=huddle_group_id)

        return render(request, 'huddle_page.html', {'huddle_group': huddle_group})
    except Account.DoesNotExist:
        # If the user does not exist, display an error message
        messages.error(request, "User not found.")
        return redirect('Huddle_app:huddle_login')

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


def save_task(request):
    if request.method == 'POST':
        # Extract task information from POST request
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        people_assigned = request.POST.get('people_assigned')
        deadline = request.POST.get('deadline')

        # Create and save new task
        new_task = Task(name=task_name, description=task_description, 
                        people_assigned=people_assigned, deadline=deadline)
        new_task.save()

        # Redirect to a success page or back to the form
        return HttpResponseRedirect(reverse('huddle_page.html'))
    else:
        # Handle non-POST request here (e.g., show an error or redirect)
        return render(request, 'your_form_template.html', {'message': 'Please submit the form.'})
