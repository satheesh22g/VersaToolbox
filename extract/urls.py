# urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('extract/', views.home, name='home'),
    path('image-extraction/', views.image_extraction, name='image_extraction'),
    path('pdf-extraction/', views.pdf_extraction, name='pdf_extraction'),
    # Other URLs within your app if needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)