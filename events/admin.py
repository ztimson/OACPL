from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmit(admin.ModelAdmin):
    fields = ['title', 'date', 'location', 'max_attendees', 'cost', 'description']
    list_display = ['title', 'date', 'location', 'max_attendees', 'cost']
