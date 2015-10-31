import itertools
from operator import attrgetter
from collections import OrderedDict
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, \
    login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from awildlife.jinja2 import custom_strftime
from dateutil import parser as date_parser

from jinja2 import Environment, FileSystemLoader

from .models import Event, Participant, Registration

import os
import pytz
from datetime import datetime

app_timezone = pytz.timezone(settings.TIME_ZONE)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    
    def __init__(self, event_dates, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['event_dates'] = forms.MultipleChoiceField(choices=event_dates)

def index(request):
    now = app_timezone.localize(datetime.now())
    events = Event.objects.filter(start_time__gte=now).order_by('start_time')
    user_messages = messages.get_messages(request)
    return render(request, 'life/index.html', {'events': events, 'messages': user_messages})

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

def register(request, event_slug):
    
    event = Event.objects.get(slug=event_slug)
    event_dates = event.schedule.occurrences()
    event_dates = [(t.strftime('%Y-%m-%d'), t.strftime('%Y-%m-%d')) \
                      for t in event_dates]

    if request.method == 'POST':
        
        form = RegisterForm(event_dates, request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data['email']
            participant, created = Participant.objects.get_or_create(email=email)
            
            if created:
                participant.first_name = form.cleaned_data['first_name']
                participant.last_name = form.cleaned_data['last_name']
                participant.save()
            
            registrations = []

            for event_date in form.cleaned_data['event_dates']:

                registration, created = \
                    Registration.objects.get_or_create(participant=participant, 
                                                       event=event,
                                                       event_date=event_date)
                
                if created:
                    registration.event_date = date_parser.parse(event_date)
                    registration.save()

                registrations.append(registration)

            sender = event.contact_info.email
            recipients = [email, event.contact_info.email]
            subject = 'You are registered for {0} with A Wild Life'.format(event.name)
            
            loader = FileSystemLoader(os.path.join(settings.BASE_DIR, 'templates'))
            env = Environment(loader=loader)
            env.filters['nice_datetime'] = custom_strftime
            email_context = {'event': event, 
                             'participant': participant, 
                             'registrations': registrations}

            text_template = env.get_template('email/register.txt')
            html_template = env.get_template('email/register.html')

            text_message = text_template.render(**email_context)
            html_message = text_template.render(**email_context)
            send_mail('Thanks for registering for {0}'.format(event.name), 
                      text_message, 
                      sender, 
                      recipients,
                      html_message=html_message)

            flash_message = "You're all registered for {0}! Look for an email with more details".format(event.name)
            messages.add_message(request, messages.INFO, flash_message) 
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm(event_dates)
    
    context = {'form': form, 'event': event, 'event_dates': event_dates}
    context.update(csrf(request))

    return render(request, 'life/register.html', context)

@login_required
def events_admin(request):
    
    events = {}
    for event in Event.objects.all():

        event_registrations = Registration.objects\
                                          .filter(event=event)\
                                          .order_by('event_date')
        
        grouper = itertools.groupby(event_registrations, 
                                    key=attrgetter('event_date'))
        
        events[event] = OrderedDict()
        for event_date, registrations in grouper:
            registrations = list(registrations)
            events[event][event_date] = [r.participant for r in registrations]
        
    return render(request, 'life/events_admin.html', {'events': events})

def login(request):
    
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return HttpResponseRedirect('/events-admin/')
        else:
            error = 'Username or password are incorrect' 
    
    return render(request, 'life/login.html', {'error': error})

def logout(request):
    django_logout(request)
    messages.add_message(request, messages.INFO, 'Successfully logged out!') 
    return HttpResponseRedirect('/')
