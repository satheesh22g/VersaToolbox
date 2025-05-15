# users/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def prompt_password_change(sender, user, request, **kwargs):
    if user.has_usable_password() and user.password == "dummy_password":
        # Redirect the user to the password change form
        # This will prompt the user to change their password on login
        # You can also force the password change here programmatically
        # For example:
        # user.set_password('new_password')
        # user.save()
        pass
