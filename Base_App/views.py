from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.cache import cache
from django.core.management import call_command
import os

# Create your views here.

def home(request):
    latest_items = ItemList.objects.order_by('-created_at')[:6]
    list = ItemCategory.objects.all()
    feedback = Feedback.objects.all()
    context = {
        'items': latest_items,
        'list':list,
        'feedback':feedback,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def menu(request):
    items = ItemList.objects.all()
    list = ItemCategory.objects.all()
    context = {
        'items': items,
        'list': list,
    }
    return render(request, 'menu.html', context)

def reservation(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone_number']
        date = request.POST['date']
        time = request.POST['time']
        total_guests = request.POST['guests']
        message = request.POST['message']
        reservation = Reservation(name=name, email=email, phone_number=phone, date=date, time=time, total_guests=total_guests, message=message)
        reservation.save()
        return render(request, 'reservation.html', {'success': 'Reservation has been made successfully!'})
    
    return render(request, 'reservation.html')


def contact(request):    
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def clear_cache(request):
    # Ensure the settings module is specified
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant_Project.settings')

    # Clear cache
    cache.clear()
    
    # Clear sessions
    call_command('clearsessions')
    
    # Clear static files cache
    # call_command('collectstatic', interactive=False, clear=True)
    
    # Clear database migrations
    call_command('migrate', fake=True)
    
    # Clear compiled files
    # call_command('compilemessages', locale='all')
    
    return HttpResponse("All caches and compiled files cleared")