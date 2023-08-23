from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import qrcode 
import png
from pyqrcode import QRCode 
from .forms import QRForm,YtMp3Form
from PIL import Image
import youtube_dl
# Create your views here.


def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def qr(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = QRForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.cleaned_data["url"]
            qr_img = qrcode.make(url)
            response = HttpResponse(content_type='image/jpeg')
            qr_img.save(response, "JPEG")    
            response['Content-Disposition'] = "attachment; filename=%s" %  "qr.jpg"
            return response
    else:
        form = QRForm()
    return render(request, "qr.html", {"form": form})

def ytmp3(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = YtMp3Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.cleaned_data["url"]
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            
                ydl.download([url])
    else:
        form = YtMp3Form()
    return render(request, "ytmp3.html", {"form": form})

