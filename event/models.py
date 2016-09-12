from __future__ import unicode_literals
# -*- coding: utf-8 -*-
__author__ = 'HappyChallenge'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import datetime_to_timestamp


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('event-warning', _('Credit')),
        ('event-info', _('Borrowing')),
        ('event-success', _('Repay')),
        ('event-inverse', _('Interest')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    # url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    css_class = models.CharField(blank=True, max_length=20, verbose_name=_('CSS Class'),
                                 choices=CSS_CLASS_CHOICES)
    start = models.DateTimeField(verbose_name=_('Start Date'))
    # end = models.DateTimeField(verbose_name=_('End Date'), blank=True, null=True)
    cre_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    upd_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    @property
    def start_timestamp(self):
        """
        Return start date as timestamp
        """
        return datetime_to_timestamp(self.start)

    # @property
    # def end_timestamp(self):
    #     """
    #     Return end date as timestamp
    #     """
    #     return datetime_to_timestamp(self.end)

    def __str__(self):
        return self.title
