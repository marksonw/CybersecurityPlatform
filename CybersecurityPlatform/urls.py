from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from research import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('research/', include('research.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)