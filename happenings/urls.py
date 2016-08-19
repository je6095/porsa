from __future__ import unicode_literals

from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^$', views.EventMonthView.as_view(), name='list'),
    url(r'^month/shift/$', views.EventMonthView.as_view(), name='month_shift'),
    url(r'^event-list/shift/$', views.EventMonthView.as_view(), name='event_list_shift'),
    url(r'^cal-and-list/shift/$', views.EventMonthView.as_view(), name='cal_and_list_shift'),
    url(r'^event/(?P<pk>[\w-]+)/$', views.EventDetailView.as_view(), name='detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d{1})/$', views.EventMonthView.as_view(), name='list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d{1})/(?P<day>\d{2}|\d{1})/$', views.EventDayView.as_view(), name='day_list'),
    url(r'^createevent/$', views.createEvent, name = 'createevent'),
    url(r'^editevent/(?P<pk>[\w-]+)/$', views.editEvent, name = 'editevent'),
    url(r'^event/(?P<pk>[\w-]+)/delete/$', views.cancelEvent, name='cancel'),
]
