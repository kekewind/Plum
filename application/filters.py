import django_filters
from .models import *



class ReportFilter(django_filters.FilterSet):
	class Meta:
		model = Report
		fields = '__all__'
		exclude = ['person', 'date_created']