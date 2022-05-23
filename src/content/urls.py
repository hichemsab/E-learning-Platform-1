from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from content.views import documents, about, contact


urlpatterns = [
    path('documents/', documents , name="documents"),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)