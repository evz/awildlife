from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pygeocoder import Geocoder, GeocoderError
from recurrence.fields import RecurrenceField
from phonenumber_field.modelfields import PhoneNumberField

EVENT_CHOICES = (
    ('movement', 'Movement'),
    ('wild-foods', 'Wild Foods'),
)

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)

    schedule = RecurrenceField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    location = models.ForeignKey('Location')
    contact_info = models.ForeignKey('ContactInfo', null=True)

    eventbrite_url = models.URLField(max_length=1000, 
                                     null=True, 
                                     blank=True)
    
    price_lower = models.FloatField(null=True, blank=True)
    price_upper = models.FloatField(null=True, blank=True)

    image = models.ImageField(height_field='image_height', 
                              width_field='image_width',
                              null=True,
                              blank=True)
    
    image_height = models.IntegerField(null=True, blank=True)
    image_width = models.IntegerField(null=True, blank=True)

    event_type = models.CharField(max_length=100, 
                                  choices=EVENT_CHOICES, 
                                  default='movement')
    
    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    event_date = models.DateField()
    event = models.ForeignKey('Event', null=True)
    participant = models.ForeignKey('Participant', null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.event.name, 
                                  self.event_date.strftime('%m/%d/%Y'))

class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField(max_length=20, 
                             null=True, 
                             blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Location(models.Model):
    name = models.CharField(max_length=255)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def geocode(self):
        try:
            results = Geocoder.geocode(self.address)
        except GeocoderError:
            results = None

        if results:
            self.latitude, self.longitude = results[0].coordinates
            self.save()

@receiver(post_save, sender=Location)
def geocode_event(sender, **kwargs):
    location = kwargs['instance']
    location.geocode()
