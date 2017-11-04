import datetime

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