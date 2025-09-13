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

# youtube
from django.views import View
from yt_dlp import YoutubeDL
import requests

def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def qr(request):
    if request.method == "POST":
        form = QRForm(request.POST)
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
            form = MobileForm(request.POST)
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
    astro_sign = None
    icon_url = None

    if request.method == "POST":
        birthdate = request.POST.get("birthdate")
        if birthdate:
            month_day = birthdate[5:] 
            if "03-21" <= month_day <= "04-19":
                astro_sign = "Aries"
                icon_url = "https://img.icons8.com/ios/452/aries.png"
            elif "04-20" <= month_day <= "05-20":
                astro_sign = "Taurus"
                icon_url = "https://img.icons8.com/ios/452/taurus.png"
            elif "05-21" <= month_day <= "06-20":
                astro_sign = "Gemini"
                icon_url = "https://img.icons8.com/ios/452/gemini.png"
            elif "06-21" <= month_day <= "07-22":
                astro_sign = "Cancer"
                icon_url = "https://img.icons8.com/ios/452/cancer.png"
            elif "07-23" <= month_day <= "08-22":
                astro_sign = "Leo"
                icon_url = "https://img.icons8.com/ios/452/leo.png"
            elif "08-23" <= month_day <= "09-22":
                astro_sign = "Virgo"
                icon_url = "https://img.icons8.com/ios/452/virgo.png"
            elif "09-23" <= month_day <= "10-22":
                astro_sign = "Libra"
                icon_url = "https://img.icons8.com/ios/452/libra.png"
            elif "10-23" <= month_day <= "11-21":
                astro_sign = "Scorpio"
                icon_url = "https://img.icons8.com/ios/452/scorpio.png"
            elif "11-22" <= month_day <= "12-21":
                astro_sign = "Sagittarius"
                icon_url = "https://img.icons8.com/ios/452/sagittarius.png"
            elif "12-22" <= month_day <= "01-19":
                astro_sign = "Capricorn"
                icon_url = "https://img.icons8.com/ios/452/capricorn.png"
            elif "01-20" <= month_day <= "02-18":
                astro_sign = "Aquarius"
                icon_url = "https://img.icons8.com/ios/452/aquarius.png"
            elif "02-19" <= month_day <= "03-20":
                astro_sign = "Pisces"
                icon_url = "https://img.icons8.com/ios/452/pisces.png"

    return render(request, "zodiac.html", {"astro_sign": astro_sign, "icon_url": icon_url})


def cricket(request):
    url = "https://www.cricbuzz.com/match-api/livescores"
    response = requests.get(url)
    data = response.json()

    live_matches = []

    for match in data.get('matches', []):
        if match.get('matchType') and match.get('status') == 'live':
            title = f"{match.get('team1')} vs {match.get('team2')}"
            score = match.get('score', 'Score not available')
            live_matches.append(f"{title}: {score}")

    if not live_matches:
        live_matches.append("No matches in progress.")

    return render(request, "cricket.html", {"live_matches": live_matches})


class YTDownloader(View):
    def __init__(self, url=None):
        self.url = url

    def get(self, request):
        return render(request, "ytdownloader.html")

    def post(self, request):
        try:
            if "fetch-vid" in request.POST:
                self.url = request.POST.get("given_url")

                ydl_opts = {"quiet": True, "noplaylist": True}
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(self.url, download=False)

                formats = [
                    {
                        "format_id": f.get("format_id"),
                        "resolution": f"{f.get('height')}p" if f.get("height") else "audio",
                        "filesize": f.get("filesize"),
                    }
                    for f in info.get("formats", [])
                    if f.get("ext") == "mp4" and (f.get("height") or f.get("acodec"))
                ]

                context = {
                    "vidTitle": info.get("title"),
                    "vidThumbnail": info.get("thumbnail"),
                    "formats": formats,
                    "url": self.url,
                }
                return render(request, "ytdownloader.html", context)

            elif "download-vid" in request.POST:
                self.url = request.POST.get("given_url")
                format_id = request.POST.get("download-vid")

                ydl_opts = {"quiet": True, "noplaylist": True}
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(self.url, download=False)

                selected_format = next(
                    (f for f in info.get("formats", []) if str(f.get("format_id")) == str(format_id)),
                    None,
                )

                if not selected_format:
                    context = {"message": "Format not found"}
                    return render(request, "ytdownloader.html", context)

                direct_url = selected_format.get("url")

                context = {
                    "vidTitle": info.get("title"),
                    "direct_url": direct_url,
                }
                return render(request, "ytdownloader.html", context)

        except Exception as e:
            context = {"message": f"Error: {str(e)}"}
            return render(request, "ytdownloader.html", context)

        return render(request, "ytdownloader.html")

def about(request):
    return render(request, "about.html")


