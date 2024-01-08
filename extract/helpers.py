import os
from django.conf import settings



def remove_tempfiles():
    media_folder = os.path.join(settings.BASE_DIR, 'media/documents')
    # Check if the folder exists
    if os.path.exists(media_folder) and os.path.isdir(media_folder):
        # Iterate over the files in the folder and delete them
        for file_name in os.listdir(media_folder):
            file_path = os.path.join(media_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                pass