# users/views.py
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.views import View
from .models import CustomUser

def user_login(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        messages.info(request, 'None')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            messages.success(request, 'Login successful!')
            if user.has_usable_password() and check_password('dummy_password', user.password):
                # Redirect the user to the password change form
                # This will prompt the user to change their password on login
                # You can also force the password change here programmatically
                # For example:
                # return redirect('password_change')
                pass
            else:
                pass  # Replace 'home' with your desired landing page
            
        else:
            messages.error(request, 'Invalid login credentials!')
            return render(request, 'login.html', {'error': 'Invalid login credentials'})


    return render(request, 'login.html')
 


def user_logout(request):
    logout(request)
    messages.warning(request, 'Logged out successfully!')
    # Optionally, remove user from session
    if 'user_id' in request.session:
        del request.session['username']
    return redirect('login')

class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request):
        user = request.user
        print(user)
        # Fetch user data or use the user_id to customize the profile page
        # user =  request.session.get('username') # Replace with your user retrieval logic

        context = {'user': user}
        return render(request, self.template_name, context)