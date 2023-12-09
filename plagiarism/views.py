from django.shortcuts import render
from .utils import check_plagiarism,calculate_marks
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
def hgandle_uploaded_file(uploaded_file):
    file_name = uploaded_file.name
    file_path = os.path.join('plagiarism', 'uploads', file_name)
    #default_storage.save('plagiarism/uploads/' + uploaded_file.name, uploaded_file)
    default_storage.save(file_path, uploaded_file)
    
    return file_path
import os
from django.conf import settings

def handle_uploaded_file(uploaded_file):
    file_name = uploaded_file.name
    file_path = os.path.join(settings.MEDIA_ROOT, 'plagiarism', 'uploads', file_name)
    
    # Check if the file exists; if it does, append a number to the filename
    if os.path.exists(file_path):
        base, ext = os.path.splitext(file_path)
        counter = 1
        while os.path.exists(file_path):
            file_path = f"{base}_{counter}{ext}"
            counter += 1
    
    with open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return file_path


def plagiarism_check(request):
    message=None
    try:
        if request.method == 'POST' and request.FILES['new_file']:
            new_file = request.FILES['new_file']
            file_path = handle_uploaded_file(new_file)
            print('file_path',file_path)
            similarity= check_plagiarism(file_path)
            print('new_file',new_file)
            marks = calculate_marks(similarity * 100)
            return render(request, 'results.html', {'similarity_score': round(similarity*100,2),'message': message,'score':marks})
        
    except Exception as e:
        print(e)
        message = "Submission Failed! Check the Document type and Try again!"

    return render(request, 'plagiarism.html',{'message':message})

def marks_calculation(request):
    return render(request, 'marks_calculation.html')
