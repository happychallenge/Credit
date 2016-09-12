from django.contrib import admin

# Register your models here.
from .models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ["title", "css_class", "start"]
    list_filler = ["title"]

admin.site.register(CalendarEvent,CalendarEventAdmin)