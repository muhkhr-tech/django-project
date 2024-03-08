#type:ignore

from django.shortcuts import render

from belanjainaja.models import *

def index(request):
    return render(request, "projects.html")