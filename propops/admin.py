from django.contrib import admin
from .models import Apartment, Booking, UserProfile

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Booking)
admin.site.register(UserProfile)