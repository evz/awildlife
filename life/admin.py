from django.contrib import admin
from .models import Event, Participant, Location, ContactInfo

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

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
