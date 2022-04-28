from django.contrib import admin
from .models import Leg, Itinerary, Agent

# Register your models here.
admin.site.site_header = "Flights Admin"
admin.site.site_title = "Flights Admin Portal"
admin.site.index_title = "Welcome to Flights Admin Portal"

admin.site.register(Leg)
admin.site.register(Itinerary)
admin.site.register(Agent)