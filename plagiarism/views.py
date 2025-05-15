import os

from django.conf import settings
from django.core.files.base import ContentFile  # noqa: F4
from django.core.files.storage import default_storage  # noqa: F4
from django.shortcuts import render

from .utils import calculate_marks, check_plagiarism

ALLOWED_FILE_TYPES = [".txt", ".docx", ".pdf"]  # Extend as needed


def is_allowed_file(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    return ext in ALLOWED_FILE_TYPES


def get_unique_file_path(directory, file_name):
    """
    Generates a unique file path to avoid overwriting existing files.
    """
    base_name, ext = os.path.splitext(file_name)
    counter = 1
    file_path = os.path.join(directory, file_name)

    while os.path.exists(file_path):
        file_path = os.path.join(directory, f"{base_name}_{counter}{ext}")
        counter += 1

    return file_path


def handle_uploaded_file(uploaded_file):
    """
    Saves uploaded file securely and returns the absolute file path.
    """
    file_name = uploaded_file.name
    directory = os.path.join(settings.MEDIA_ROOT, "plagiarism", "uploads")

    os.makedirs(directory, exist_ok=True)

    file_path = get_unique_file_path(directory, file_name)

    with open(file_path, "wb+") as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return file_path


def plagiarism_check(request):
    message = None
    context = {"message": message}

    if request.method == "POST":
        uploaded_file = request.FILES.get("new_file")

        if not uploaded_file:
            context["message"] = "No file uploaded."
            return render(request, "plagiarism.html", context)

        if not is_allowed_file(uploaded_file.name):
            context["message"] = (
                "Unsupported file type. Please upload a .txt, .pdf, or .docx file."
            )
            return render(request, "plagiarism.html", context)

        try:
            file_path = handle_uploaded_file(uploaded_file)
            similarity_score = check_plagiarism(file_path)
            score = calculate_marks(similarity_score * 100)

            context.update(
                {
                    "similarity_score": round(similarity_score * 100, 2),
                    "score": score,
                    "file_name": uploaded_file.name,
                }
            )
            return render(request, "results.html", context)

        except Exception as e:
            print(f"Error during plagiarism check: {e}")
            context["message"] = (
                "Submission failed. Ensure the file is valid and try again."
            )

    return render(request, "plagiarism.html", context)


def marks_calculation(request):
    return render(request, "marks_calculation.html")
