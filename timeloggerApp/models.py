from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):

    emp_first_name = models.CharField(max_length=200)
    emp_last_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    emp_number = models.IntegerField('emp_number')

    def __str__(self):
        return self.emp_first_name

class TimeLog(models.Model):
    emp_number = models.IntegerField('emp_number')
    timeStamp = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
