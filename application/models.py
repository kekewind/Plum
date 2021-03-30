from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
            return self.name

    @property
    def reports(self):
        report_count = self.report_set.all().count()
        return str(report_count)



class Unit(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Report(models.Model):
   
    STATUS = (
            ('Warning', 'Warning'),
            ('Repairing', 'Repairing'),
            ('Normal', 'Normal'),
            ) 
    
    person = models.ForeignKey(Person, on_delete= models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, on_delete= models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    details = models.TextField()
    
    def __str__(self):
        return str(self.unit)