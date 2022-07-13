from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello supercool_5</h1>")

def about(request):
    return HttpResponse("supercool you are amazing")