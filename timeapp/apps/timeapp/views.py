from django.shortcuts import render
from time import strftime, localtime

def index(request): # couldn't get to work with datetime so followed
    date_time = {   # Keith's example!
        'date': strftime('%b %d, %Y'),
        'time': strftime('%I:%M %p', localtime())
    }
    return render(request, 'timeapp/index.html', date_time)
