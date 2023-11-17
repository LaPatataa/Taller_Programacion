"""
URL configuration for Portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path("", inicio),
    path("resumen/", resumen),
    path("", include('Aplicaciones.proyectos.urls')),
    path("", include('Aplicaciones.contacto.urls')),
    path("", include('Aplicaciones.ubicaciones.urls')),
    path("", include('Aplicaciones.qr_app.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
