from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from .models import TimeLog
import datetime
import time
# Views here.
from matplotlib import pyplot as plt
def showTime(request):
    emp_list = Employee.objects.get(id=id)
    return HttpResponse("<h1>I am here</h1>")

def index(request):
    id = 555
    emp_list = Employee.objects.get(id=id)
    template = loader.get_template('timeloggerApp/index.html')
    currentDate = str(datetime.date.today())
    currentTime = str(time.ctime())

    context = {

        'current_date': currentDate,
        'current_time' : currentTime,
        'emp_first_name': emp_list.emp_first_name,
        'emp_last_name': emp_list.emp_last_name,
        'current_id': id,

    }

    return HttpResponse(template.render(context,request))

def clockIn(request,id):

    time_log = TimeLog(emp_number=id)
    time_log.save()

