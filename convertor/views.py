from django.http import HttpResponse
from django.shortcuts import render, redirect
import img2pdf
import string
import random
import os
from zipfile import ZipFile
import string
import fitz
from PIL import Image
from docx2pdf import convert

# Create your views here.
def convert_home(request):
    return render(request, 'convert_index.html')

def jpgToPdf(request):
    if request.method == "POST":
        # Creating a random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./convertor/static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload, exist_ok=True)
        
        # Saving uploaded JPG files
        files = request.FILES
        files_list = [file for file in files.getlist('files')]
        
        # Convert JPG files to PDF
        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        pdf_path = os.path.join(path_to_upload, "sample.pdf")
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        
        # Provide the PDF file for download
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="converted_file.pdf"'
                return response
        else:
            return HttpResponse("Conversion failed or file not found.")
    
    return render(request, 'jpgtopdf.html')





def pdftojpg(request):
    if request.method == "POST":
        # Creating a random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./convertor/static/uploaded_files/pdf2jpg', str(res))
        os.makedirs(path_to_upload, exist_ok=True)

        files = request.FILES
        for file in files.getlist('files'):
            with open(os.path.join(path_to_upload, 'sample.pdf'), 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        pdf_path = os.path.join(path_to_upload, 'sample.pdf')
        pdf_document = fitz.open(pdf_path)
        
        images = []
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_path = os.path.join(path_to_upload, f'page{page_num}.jpg')
            img.save(img_path, "JPEG")
            images.append(img_path)

        pdf_document.close()

        # Creating a zip file containing the images
        zip_file_path = os.path.join(path_to_upload, 'sample.zip')
        with ZipFile(zip_file_path, 'w') as zipObj:
            for image in images:
                zipObj.write(image, os.path.basename(image))
                os.remove(image)

        # Provide the zip file for download
        if os.path.exists(zip_file_path):
            with open(zip_file_path, 'rb') as zip_file:
                response = HttpResponse(zip_file.read(), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="converted_images.zip"'
                return response
        else:
            return HttpResponse("Conversion failed or file not found.")

    return render(request, 'pdftojpg.html')




def doctopdf(request):
    if request.method == "POST":
        # Creating a random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./convertor/static/uploaded_files/doc2pdf', str(res))
        os.makedirs(path_to_upload, exist_ok=True)

        files = request.FILES
        for file in files.getlist('files'):
            with open(os.path.join(path_to_upload, 'sample.docx'), 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        docx_path = os.path.join(path_to_upload, 'sample.docx')
        pdf_path = os.path.join(path_to_upload, 'converted_file.pdf')

        # Convert DOCX to PDF using docx2pdf
        try:
            convert(docx_path, pdf_path)
        except Exception as e:
            return HttpResponse(f"Conversion failed: {e}")

        # Provide the PDF file for download
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="converted_file.pdf"'
                return response
        else:
            return HttpResponse("Conversion failed or file not found.")

    return render(request, 'doctopdf.html')
