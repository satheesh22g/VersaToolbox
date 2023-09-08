from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import qrcode
from .forms import QRForm,YtMp3Form,MobileForm,ZodiacForm
from PIL import Image
import youtube_dl
import phonenumbers
from phonenumbers import carrier, geocoder,timezone
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


def mobile_number(request):
    mobileno=None
    cr=None
    tz=None
    country =None
    valid = None
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MobileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            number = "+"+str(form.cleaned_data["number"])
            print(number)
            mobileno=phonenumbers.parse(number)
            tz = timezone.time_zones_for_number(mobileno)[0]
            cr = carrier.name_for_number(mobileno,"en")
            country = geocoder.description_for_number(mobileno,"en")
            valid = phonenumbers.is_valid_number(mobileno)

    else:
        form = MobileForm()
    return render(request, "mobile_number.html", {"form": form,"mobileno":mobileno,"cr":cr,"tz":tz,"country":country,"valid":valid})




def zodiac_sign(request):
    astro_sign=None
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ZodiacForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            date_input = form.cleaned_data["date_input"]
            day = int(date_input.strftime("%d"))
            month = int(date_input.strftime("%m"))
            if month == 12: 
                astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
            elif month == 1: 
                astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
            elif month == 2: 
                astro_sign = 'Aquarius' if (day < 19) else 'pisces'
            elif month == 3: 
                astro_sign = 'Pisces' if (day < 21) else 'aries'
            elif month == 4: 
                astro_sign = 'Aries' if (day < 20) else 'taurus'
            elif month == 5: 
                astro_sign = 'Taurus' if (day < 21) else 'gemini'
            elif month == 6: 
                astro_sign = 'Gemini' if (day < 21) else 'cancer'
            elif month == 7: 
                astro_sign = 'Cancer' if (day < 23) else 'leo'
            elif month == 8: 
                astro_sign = 'Leo' if (day < 23) else 'virgo'
            elif month == 9: 
                astro_sign = 'Virgo' if (day < 23) else 'libra'
            elif month == 10: 
                astro_sign = 'Libra' if (day < 23) else 'scorpio'
            elif month == 11: 
                astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
            print(astro_sign)
    else:
        form = ZodiacForm()
    return render(request, "zodiac.html", {"form": form,"astro_sign":astro_sign})

def about(request):
    return render(request, "about.html")
