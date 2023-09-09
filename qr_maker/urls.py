from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.dashboard),
    path('qr/',views.qr),
    path('ytmp3/',views.ytmp3),
    path('mobile_number/',views.mobile_number),
    path('zodiac_sign/',views.zodiac_sign),
    path('about/',views.about),
    path('cricket/',views.cricket),
    path('home/',views.home.as_view(),name="home"),
]
