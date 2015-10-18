from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseNotFound
from .models import Event
import pytz
from datetime import datetime

app_timezone = pytz.timezone(settings.TIME_ZONE)

def index(request):
    now = app_timezone.localize(datetime.now())
    events = Event.objects.filter(start_time__gte=now).order_by('start_time')
    return render(request, 'life/index.html', {'events': events})

def movement(request):
    
    events = Event.objects\
                  .filter(event_type='movement')\
                  .order_by('-start_time')

    return render(request, 'life/movement.html', {'events': events})

def wild_foods(request):
    
    events = Event.objects\
                  .filter(event_type='wild_foods')\
                  .order_by('-start_time')

    return render(request, 'life/wild_foods.html', {'events': events})

def event_detail(request, year, month, day, slug):
    
    event = Event.objects.filter(start_time__year=year)\
                        .filter(start_time__month=month)\
                        .filter(start_time__day=day)\
                        .filter(slug=slug)\
                        .first()

    if event:
        return render(request, 'life/event-detail.html', {'event': event})
    
    return HttpResponseNotFound()

