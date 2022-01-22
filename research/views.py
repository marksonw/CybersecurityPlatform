from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def project(req, pk):
    return HttpResponse("Single Project" + ' ' + str(pk))