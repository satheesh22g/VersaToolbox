import os
import random
import string
from zipfile import ZipFile

import fitz  # PyMuPDF
import img2pdf
from django.http import HttpResponse
from django.shortcuts import render
from docx2pdf import convert
from PIL import Image

# === Utility Functions ===


def random_folder(base_dir, subfolder):
    folder = "".join(random.choices(string.ascii_lowercase, k=10))
    path = os.path.join(base_dir, subfolder, folder)
    os.makedirs(path, exist_ok=True)
    return path


def save_uploaded_files(files, dest_path, base_name="sample", ext=""):
    file_paths = []
    for idx, file in enumerate(files):
        filename = f"{base_name}{idx}{ext}"
        full_path = os.path.join(dest_path, filename)
        with open(full_path, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)
        file_paths.append(full_path)
    return file_paths


# === Views ===


def convert_home(request):
    return render(request, "convert_index.html")


def jpgToPdf(request):
    if request.method == "POST":
        upload_dir = random_folder("./convertor/static/uploaded_files", "jpg2pdf")

        jpg_files = request.FILES.getlist("files")
        if not jpg_files:
            return HttpResponse("No files uploaded.")

        try:
            a4_size = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
            layout_fun = img2pdf.get_layout_fun(a4_size)
            pdf_path = os.path.join(upload_dir, "converted.pdf")

            with open(pdf_path, "wb") as f:
                f.write(img2pdf.convert(jpg_files, layout_fun=layout_fun))

            with open(pdf_path, "rb") as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type="application/pdf")
                response["Content-Disposition"] = (
                    'attachment; filename="converted_file.pdf"'
                )
                return response

        except Exception as e:
            return HttpResponse(f"Conversion failed: {e}")

    return render(request, "jpgtopdf.html")


def pdftojpg(request):
    if request.method == "POST":
        upload_dir = random_folder("./convertor/static/uploaded_files", "pdf2jpg")

        pdf_files = save_uploaded_files(
            request.FILES.getlist("files"), upload_dir, "sample", ".pdf"
        )
        if not pdf_files:
            return HttpResponse("No files uploaded.")

        images = []
        try:
            pdf_document = fitz.open(pdf_files[0])
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img_path = os.path.join(upload_dir, f"page{page_num}.jpg")
                img.save(img_path, "JPEG")
                images.append(img_path)
            pdf_document.close()
        except Exception as e:
            return HttpResponse(f"Error converting PDF to images: {e}")

        # Create zip of all images
        zip_path = os.path.join(upload_dir, "images.zip")
        try:
            with ZipFile(zip_path, "w") as zipf:
                for img_path in images:
                    zipf.write(img_path, os.path.basename(img_path))
                    os.remove(img_path)

            with open(zip_path, "rb") as zip_file:
                response = HttpResponse(zip_file.read(), content_type="application/zip")
                response["Content-Disposition"] = (
                    'attachment; filename="converted_images.zip"'
                )
                return response
        except Exception as e:
            return HttpResponse(f"Failed to zip images: {e}")

    return render(request, "pdftojpg.html")


def doctopdf(request):
    if request.method == "POST":
        upload_dir = random_folder("./convertor/static/uploaded_files", "doc2pdf")

        docx_files = save_uploaded_files(
            request.FILES.getlist("files"), upload_dir, "doc", ".docx"
        )
        pdf_paths = []

        try:
            for docx_path in docx_files:
                base = os.path.splitext(docx_path)[0]
                pdf_path = base + ".pdf"
                convert(docx_path, pdf_path)
                pdf_paths.append(pdf_path)
                os.remove(docx_path)  # Cleanup

            # Zip multiple PDFs
            zip_path = os.path.join(upload_dir, "converted.zip")
            with ZipFile(zip_path, "w") as zipf:
                for pdf in pdf_paths:
                    zipf.write(pdf, os.path.basename(pdf))
                    os.remove(pdf)

            with open(zip_path, "rb") as zip_file:
                response = HttpResponse(zip_file.read(), content_type="application/zip")
                response["Content-Disposition"] = (
                    'attachment; filename="converted_pdfs.zip"'
                )
                return response

        except Exception as e:
            return HttpResponse(f"Conversion failed: {e}")

    return render(request, "doctopdf.html")
