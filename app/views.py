from django.shortcuts import render
from .models import Race
from .models import Driver

def race_list(request):
    races = Race.objects.all()  # Fetch all races from the database
    return render(request, 'race_list.html', {'races': races})

def driver_list(request):
    drivers = Driver.objects.all() # Fetch all drivers from the database
    return render(request, 'driver_lsit.html', {'drivers': drivers})