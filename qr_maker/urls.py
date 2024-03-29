from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('qr/',views.qr),
    path('mobile_number/',views.mobile_number),
    path('zodiac_sign/',views.zodiac_sign),
    path('about/',views.about),
    path('cricket/',views.cricket),
    path('ytdownloader/', views.YTDownloader.as_view(), name="ytdownloader"),
]
