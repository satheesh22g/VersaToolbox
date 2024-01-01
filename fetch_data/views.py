from django.shortcuts import render
from api.models import ContactMessage  # Import your ContactMessage model from the original app

def display_contact_messages(request):
    messages = ContactMessage.objects.all()  # Fetch all ContactMessage data
    return render(request, 'messages.html', {'messages': messages})
