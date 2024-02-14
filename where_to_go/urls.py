from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places.views import show_places, show_place_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_places),
    path('place/<int:place_id>/', show_place_id, name='show_place_id'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
