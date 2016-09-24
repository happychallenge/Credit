# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import url
from .views import CalendarJsonListView, event_calendar

urlpatterns = [
    # url(r'^$', CalendarView.as_view(), name='calendar'),
    url(r'^$', event_calendar, name='calendar'),
    url(r'^json/$', CalendarJsonListView.as_view(), name='calendar_json'),
]
