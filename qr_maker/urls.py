from django.urls import path

from . import views
from .views import ConvertPDFToDOCXView

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.dashboard),
    path('qr/',views.qr),
    path('ytmp3/',views.ytmp3),
    path('mobile_number/',views.mobile_number),
    path('zodiac_sign/',views.zodiac_sign),
    path('about/',views.about),
    path('cricket/',views.cricket),
    #path('convert/', views.convert_pdf_to_docx, name='convert_pdf_to_docx'),
    path('convert_pdf_to_docx/', ConvertPDFToDOCXView.as_view(), name='convert_pdf_to_docx'),
    path('ytdownloader/', views.YTDownloader.as_view(), name="ytdownloader"),
    #path('ytdownloader/',views.ytdownloader.as_view(),name="ytdownloader"),
]
