from places import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:id>', views.post_detail, name="place_detail"),
    path('tinymce/', include('tinymce.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
