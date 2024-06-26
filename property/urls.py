"""
URL configuration for property project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from propops.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),
    path('apartment/', apartment, name='apartment'),
    path('apartment_detail/<int:apartment_id>/', apartment_detail, name='apartment_detail'),
    path('book_apartment/<int:apartment_id>/', book_apartment, name='book_apartment'),
    path('booking_success/', booking_success, name='booking_success'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()