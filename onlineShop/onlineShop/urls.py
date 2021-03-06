"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import header
from .views import home_page, productSearch

urlpatterns = [
    path('', home_page),
    path('', include('Library.urls')),
    path('', include('Account.urls')),
    path('', include('Stationery.urls')),
    path('', include('Calture.urls')),
    path('', include('Order.urls')),
    path('', include('Contact_us.urls')),
    path('api/', include('Library.api.urls')),
    path('api/', include('Calture.api.urls')),
    path('api/', include('Stationery.api.urls')),
    path('header', header, name='header'),
    path('admin/', admin.site.urls),
    path('search', productSearch),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
                  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
                  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
