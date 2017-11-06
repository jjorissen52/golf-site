import datetime
import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer

class UpcomingEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(start__gt=datetime.datetime.now())
    serializer_class = EventSerializer

class CalendarView(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        kwargs.update(super(CalendarView, self).get_context_data(**kwargs))
        kwargs["events"] = Event.objects.filter(start__gt=datetime.datetime.now()).values('title', 'start', 'end', 'description', 'id')
        return kwargs