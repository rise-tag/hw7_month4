# app/views.py
from django.http import HttpResponse

def settings(request):
    return HttpResponse("Settings page")
