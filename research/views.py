from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def research(request):
    return render(request, 'research/research.html')
