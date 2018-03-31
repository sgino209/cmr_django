# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Motzkin URL Configuration
# The `urlpatterns` list routes URLs to views.

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Use include() to add URLS from the catalog application and authentication system
# Add URL maps to redirect the base URL to our application
# Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)