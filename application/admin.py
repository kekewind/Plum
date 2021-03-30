from django.contrib import admin

#from .models import *
from . models import Person, Report, Unit

admin.site.register(Person)
admin.site.register(Unit)
admin.site.register(Report)