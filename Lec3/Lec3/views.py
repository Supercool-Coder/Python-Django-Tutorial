from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello supercool")

def useful1(request):
    return HttpResponse('''  <a 
    href="https://practice.geeksforgeeks.org/contest/job-a-thon-10-hiring-challenge/instructions" >code with 
    supercool</a>''')