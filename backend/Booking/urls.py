"""
URL configuration for Booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from .views import GetCSRFToken

schema_view = get_swagger_view(title="Hostel Booking App")

admin.site.site_header = "Hostel Booking Admin"
admin.site.site_title = "Hostel Booking Admin Portal"
admin.site.index_title = "Welcome to Hostel Booking Admin Portal"

urlpatterns = [
    path("csrf/", GetCSRFToken.as_view(), name="get-csrf-token"),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path('hostel-back-office/', admin.site.urls),
    path('authenticate/', include('authentication.urls')),
    path('hostel/',include('hostel.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)