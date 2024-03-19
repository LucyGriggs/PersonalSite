from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime

from .models import Race
from .models import Driver

# Create your views here.

def race_list(request):
    races = Race.objects.all()  # Fetch all races from the database
    return render(request, 'race_list.html', {'races': races})

def driver_list(request):
    drivers = Driver.objects.all() # Fetch all drivers from the database
    return render(request, 'driver_list.html', {'drivers': drivers})

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About Page',
            'year':datetime.now().year,
        }
    )
