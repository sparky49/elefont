from django.shortcuts import render
from django.http import HttpResponse

def elefont(request):
    return HttpResponse("<h1>My name is elefont</h1>")
  
# Create your views here.
