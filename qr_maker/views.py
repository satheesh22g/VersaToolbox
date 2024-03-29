from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from .forms import QRForm,MobileForm,ZodiacForm
import phonenumbers
from phonenumbers import carrier, geocoder,timezone
import requests
from bs4 import BeautifulSoup
from django.views.generic import View
from django.http import HttpResponse
from django.views import View

# youtuble

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
from django.http import StreamingHttpResponse
from pytube import YouTube
import requests

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



def mobile_number(request):
    message = None
    mobileno=None
    cr=None
    tz=None
    country =None
    valid = None
    try:
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
    except:
        message="Invalid Number, Try Again"
        return render(request, "mobile_number.html", {"form": form,"message":message})
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

def cricket(request):
    live_matches=['8746rtur']
    page = requests.get('http://static.cricinfo.com/rss/livescores.xml') # HTTP Get request to cricinfo rss feed
    soup = BeautifulSoup(page.text,'lxml')
    matches = soup.find_all('description') # description tags contain the score
    live_matches = [s.get_text() for s in matches if '*' in s.get_text()]
    return render(request, "cricket.html",{"live_matches":live_matches})


class YTDownloader(View):
    def __init__(self, url=None):
        self.url = url

    def get(self, request):
        return render(request, 'ytdownloader.html')

    def post(self, request):
        try:
            if 'fetch-vid' in request.POST:
                self.url = request.POST.get('given_url')
                video = YouTube(self.url)
                vid_title, vid_thumbnail = video.title, video.thumbnail_url
                qual, stream = [], []
                for vid in video.streams.filter(progressive=True):
                    qual.append(vid.resolution)
                    stream.append(vid)
                context = {'vid_title': vid_title, 'vid_thumbnail': vid_thumbnail,
                           'qual': qual, 'stream': stream,
                           'url': self.url}
                return render(request, 'ytdownloader.html', context)

            elif 'download-vid' in request.POST:
                self.url = request.POST.get('given_url')
                video = YouTube(self.url)
                video_qual = video.streams[int(request.POST.get('download-vid')) - 1]

                # Sanitize the video title for use as a file name
                title = ''.join(c if c.isalnum() or c in [' ', '_'] else '' for c in video.title)
                title = title.replace(' ', '_')

                # Download the video content using requests
                video_data = requests.get(video_qual.url).content

                # Prepare the file for download using StreamingHttpResponse
                response = StreamingHttpResponse([video_data], content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{title}.mp4"'
                return response

        except (RegexMatchError, VideoUnavailable) as e:
            context = {'message': f"Error: {str(e)}. Try again!!!"}
            return render(request, 'ytdownloader.html', context)

        return render(request, 'ytdownloader.html')


def about(request):
    return render(request, "about.html")


