from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello supercool sir")

def removepunc(request):
    return HttpResponse("This line is going to remove punctuation")

def capfirst(request):
    return HttpResponse("This line is going to capitalize all stings")

def newline(request):
    return HttpResponse("This line is going to print new line in text area")

