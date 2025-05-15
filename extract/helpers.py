import logging
import os

from django.conf import settings

logger = logging.getLogger(__name__)


def remove_tempfiles():
    media_folder = os.path.join(settings.BASE_DIR, "media/documents")
    if os.path.exists(media_folder) and os.path.isdir(media_folder):
        for file_name in os.listdir(media_folder):
            file_path = os.path.join(media_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                logger.warning(f"Failed to delete {file_path}: {e}")
