# -*- coding: utf-8 -*-
from django.http import request

__author__ = 'sandlbn and w3lly'

import datetime
from django.views.generic import ListView, TemplateView
from .models import CalendarEvent
from .serializers import event_serializer
from .utils import timestamp_to_datetime

class CalendarView(TemplateView):
    template_name = 'event/calendar.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(TemplateView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     request.session['today'] = datetime.date.today()
    #     return context

class CalendarJsonListView(ListView):
    template_name = 'event/calendar_events.html'

    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date) + datetime.timedelta(-30),
                    timestamp_to_datetime(to_date)
                    )
            )
        elif from_date:
            queryset = queryset.filter(
                start__gte=timestamp_to_datetime(from_date)
            )
        elif to_date:
            queryset = queryset.filter(
                end__lte=timestamp_to_datetime(to_date)
            )

        return event_serializer(queryset)


