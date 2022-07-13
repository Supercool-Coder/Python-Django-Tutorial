from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def remove(request):
    return HttpResponse("welcome supercool sir")