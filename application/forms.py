from django.forms import ModelForm
from .models import Person, Report

class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = '__all__'