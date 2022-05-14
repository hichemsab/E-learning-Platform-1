from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from content.views import documents


urlpatterns = [
    path('documents/', documents , name="documents"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)