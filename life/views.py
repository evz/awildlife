from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
from django.template.context_processors import csrf
from awildlife.jinja2 import custom_strftime

from jinja2 import Environment, FileSystemLoader

from .models import Event, Participant

import os
import pytz
from datetime import datetime

app_timezone = pytz.timezone(settings.TIME_ZONE)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()


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

    if request.method == 'POST':
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            
            email = form.cleaned_data['email']
            participant, created = Participant.objects.get_or_create(email=email)
            
            if created:
                participant.first_name = form.cleaned_data['first_name']
                participant.last_name = form.cleaned_data['last_name']
            
            participant.event_set.add(event)
            participant.save()

            sender = event.contact_info.email
            recipients = [email, event.contact_info.email]
            subject = 'You are registered for {0} with A Wild Life'.format(event.name)
            
            loader = FileSystemLoader(os.path.join(settings.BASE_DIR, 'templates'))
            env = Environment(loader=loader)
            env.filters['nice_datetime'] = custom_strftime
            email_context = {'event': event, 'participant': participant}

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
        form = RegisterForm()
    
    context = {'form': form, 'event': event}
    context.update(csrf(request))

    return render(request, 'life/register.html', context)

