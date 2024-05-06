from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Apartment, Booking, UserProfile
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        user = User.objects.create_user(username=username, email=email, password=password)

      
        request.session['signup_username'] = username
        request.session['signup_email'] = email
        request.session['signup_password'] = password

        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
           
            auth_login(request, user)
            messages.success(request, 'You have successfully signed up!')
            return redirect('login')  

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

       
        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'login.html')

@login_required
def signout(request):
    django_logout(request)
    return redirect('home') 

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        # Update profile fields
        user_profile.phone = phone
        user_profile.address = address
        if image:
            user_profile.image = image

        user_profile.save()
        messages.success(request, 'Profile updated successfully')

    return render(request, 'profile.html', {'user_profile': user_profile})


def apartment(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartment.html', {'apartments': apartments})

def apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    return render(request, 'apartmentdetail.html', {'apartment': apartment})

@login_required
def book_apartment(request, apartment_id):
    if request.method == 'POST':
        user = request.user
        apartment = Apartment.objects.get(pk=apartment_id)
        contact_number = request.POST.get('phone')
        booking_date = timezone.now() 
        total_price = apartment.price  
        
        
        booking = Booking.objects.create(
            user=user,
            apartment=apartment,
            contact_number=contact_number,
            booking_date=booking_date,
            total_price=total_price
        )
        
        booking.save()
        apartment.delete()

        return redirect('booking_success')  
    else:
       
        apartment = Apartment.objects.get(pk=apartment_id)
        return render(request, 'booking.html', {'apartment': apartment})

def booking_success(request):
    return render(request, 'booking_success.html')