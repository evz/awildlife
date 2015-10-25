from django.contrib import admin
from .models import Event, Participant, Location, ContactInfo

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    exclude = ('eventbrite_url',
               'image_height',
               'image_width',)

class ParticipantAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class ContactInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
