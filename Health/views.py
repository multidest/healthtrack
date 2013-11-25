from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Health index.")
    
def detail(request, patient_id):
    return HttpResponse("You're looking at %s." % patient_id)

def results(request, patient_id):
    return HttpResponse("You're looking at the results of %s." % patient_id)

def vote(request, patient_id):
    return HttpResponse("You're voting on %s." % patient_id)