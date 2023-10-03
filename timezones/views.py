from django.shortcuts import render
from datetime import datetime
import pytz

# A4 part 2 assignment - pablo duenas
def show_time(request):
    # Define the time zones you want to display
    timezone1 = pytz.timezone('Europe/London')
    timezone2 = pytz.timezone('America/New_York')

    # Get the current time in the specified time zones
    time1 = datetime.now(timezone1)
    time2 = datetime.now(timezone2)

    context = {
        'time1': time1,
        'time2': time2,
    }

    return render(request, 'show_time.html', context)
