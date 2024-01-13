from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from api.models import ContactMessage

def display_contact_messages(request):
        messages = ContactMessage.objects.all()
        
        print(request.session.get('user_id'))
        return render(request, 'messages.html', {'messages': messages})
def mark_as_read(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(ContactMessage, id=message_id)
        message.read = True
        message.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
