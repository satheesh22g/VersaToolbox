# users/views.py
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.views import View
from .models import CustomUser
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password



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

@user_passes_test(lambda u: u.is_superuser)
def admin_user_management(request):
    users = CustomUser.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create_user':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')  # You may want to validate and hash the password

            try:
                user = CustomUser.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password),
                )
                messages.success(request, 'User created successfully!')
            except Exception as e:
                messages.error(request, f'User creation failed. {str(e)}')

        elif action == 'delete':
            user_id = request.POST.get('user_id')
            try:
                user = CustomUser.objects.get(id=user_id)
                user.delete()
                messages.success(request, 'User deleted successfully!')
            except CustomUser.DoesNotExist:
                messages.error(request, 'User not found!')

        elif action == 'reset_password':
            user_id = request.POST.get('user_id')
            try:
                user = CustomUser.objects.get(id=user_id)
                user.set_password('versatoolbox')
                user.save()
                messages.success(request, 'Password reset successfully!')
            except CustomUser.DoesNotExist:
                messages.error(request, 'User not found!')

        return redirect('admin_user_management')

    context = {'users': users}
    return render(request, 'admin_user_management.html', context)


def password_change(request):
    if request.method == 'POST':
        # Ensure the user is authenticated before changing the password
        if request.user.is_authenticated:
            print(2)
            # Manually set the password
            new_password = request.POST.get('cpassword')
            request.user.set_password(new_password)
            request.user.save()
            print(3)
            # Update the session to prevent the user from being logged out
            update_session_auth_hash(request, request.user)
            print("success")

            messages.success(request, 'Password changed successfully!')
            return redirect('profile')
        else:
            print(5)
            messages.error(request, 'User is not authenticated.')
    else:
        print(6)
        messages.error(request, 'Invalid form submission. Please correct the errors.')

    return render(request, 'change_password.html')
