"""
URL configuration for Restaurant_Project project.

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
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('authentication.urls')),
    path('', home, name='Home'),
    path('about/', about, name='About'),
    path('menu/', menu, name='Menu'),
    path('reservation/', reservation, name='Reservation'),
    path('contact/', contact, name='Contact'),
    path('login/', login, name='Login'),
    path('signup/', signup, name='SignUp'),
    path('clear/', clear_cache, name='clear_cache'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
