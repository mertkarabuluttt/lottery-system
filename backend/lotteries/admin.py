from django.contrib import admin

from .models import Event, Participant, Ballot

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Ballot)
