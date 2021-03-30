from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ReportForm
from . filters import ReportFilter

#-------------------(DETAIL/LIST VIEWS) -------------------

def dashBoard(request):
	reports = Report.objects.all().order_by('-status')[0:5]
	persons = Person.objects.all()

	total_persons = persons.count()

	total_reports = Report.objects.all().count()
	repairing = Report.objects.filter(status='Repairing').count()
	warning = Report.objects.filter(status='Warning').count()



	context = {'persons':persons, 'reports':reports,
	'total_persons':total_persons,'total_reports':total_reports, 
	'repairing':repairing, 'warning':warning}
	return render(request, 'dashBoard.html', context)

def units(request):
	units = Unit.objects.all()
	context = {'units': units}
	return render(request, 'units.html', context)

def person(request, pk):
	person = Person.objects.get(id=pk)
	reports = person.report_set.all()
	total_reports = reports.count()



	reportFilter = ReportFilter(request.GET, queryset=reports) 
	reports = reportFilter.qs

	context = {'person':person, 'reports':reports, 'total_reports':total_reports,
	'filter':reportFilter}
	return render(request, 'person.html', context)


#-------------------(CREATE VIEWS) -------------------

def createReport(request):
	action = 'create'
	form = ReportForm()
	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'action':action, 'form':form}
	return render(request, 'report_form.html', context)

#-------------------(UPDATE VIEWS) -------------------

def updateReport(request, pk):
	action = 'update'
	report = Report.objects.get(id=pk)
	form = ReportForm(instance=report)

	if request.method == 'POST':
		form = ReportForm(request.POST, instance=report)
		if form.is_valid():
			form.save()
			return redirect('/user/' + str(report.person.id))

	context =  {'action':action, 'form':form}
	return render(request, 'report_form.html', context)

#-------------------(DELETE VIEWS) -------------------

def deleteReport(request, pk):
	report = Report.objects.get(id=pk)
	if request.method == 'POST':
		person_id = report.person.id
		person_url = '/user/' + str(person_id)
		report.delete()
		return redirect(person_url)
		
	return render(request, 'delete_unit.html', {'item':report})
