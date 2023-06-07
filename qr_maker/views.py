from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import qrcode 
import png
from pyqrcode import QRCode 
from .forms import NameForm
from PIL import Image

# Create your views here.


def index(request):
    return render(request,'index.html')

def qr(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.cleaned_data["url"]
            qr_img = qrcode.make(url)
            response = HttpResponse(content_type='image/jpeg')
            qr_img.save(response, "JPEG")    
            response['Content-Disposition'] = "attachment; filename=%s" %  "qr.jpg"
            return response
    else:
        form = NameForm()
    return render(request, "qr.html", {"form": form})