# users/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import update_session_auth_hash

@receiver(user_logged_in)
def prompt_password_change(sender, user, request, **kwargs):
    if user.has_usable_password() and user.password == 'dummy_password':
        # Redirect the user to the password change form
        # This will prompt the user to change their password on login
        # You can also force the password change here programmatically
        # For example:
        # user.set_password('new_password')
        # user.save()
        pass
