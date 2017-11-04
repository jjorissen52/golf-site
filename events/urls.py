from django.conf.urls import url

from events import views

urlpatterns = [
    url(r'^$', views.CalendarView.as_view(), name='calendar'),
]