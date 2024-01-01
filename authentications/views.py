from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User
from .auths import CustomAuthBackend 
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm  # Import your LoginForm
from .models import User

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user using the custom authentication backend
            user = CustomAuthBackend().authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard URL name
            else:
                # Invalid credentials
                # Handle invalid login (display error message, etc.)
                pass
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
