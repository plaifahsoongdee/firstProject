from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>My First Django APP!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current Date & time:</b> " + str(dt)
    return HttpResponse(s)

# Create your views here.
