from django.shortcuts import render

from .models import Race
from .models import Driver

# Create your views here.

def race_list(request):
    races = Race.objects.all()  # Fetch all races from the database
    return render(request, 'race_list.html', {'races': races})

def driver_list(request):
    drivers = Driver.objects.all() # Fetch all drivers from the database
    return render(request, 'driver_lsit.html', {'drivers': drivers})


#TESTING
def index(request):
    now = datetime.now()

    return render(
        request,
        "app/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )