from django.http import JsonResponse
from django.shortcuts import render

from .models import Attendees, Event


def view(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


def register(request):
    event = Event.objects.get(id=request.POST.get('id'))
    attendee = Attendees(name='{} {}'.format(request.user.first_name, request.user.last_name), paid=False)
    attendee.save()
    event.attendees.add(attendee)
    event.save()
    return JsonResponse({'success': True})
