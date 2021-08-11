from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    """
    Displays a form for new account registration.
    Validates username and password.
    Creates a new account with the information from the registration form.
    """
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )

                    user.save()
                    # Redirects to login page
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    """
    Displays a login form for accounts.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome')
            # Directs user to dashboard if login is successful.
            return redirect('dashboard')
        else:
            messages.error(request, 'Username/Password do not match')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """
    View for logging out.
    """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out')
        # Directs user to home page if logout is successful.
        return redirect('index')


def dashboard(request):
    """
    Dashboard view that lists all Contact objects.
    """
    user_contacts = Contact.objects.order_by('-inquiry_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
