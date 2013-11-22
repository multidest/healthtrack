# Create your views here.


from django.http import HttpResponse

def index (Request):
    return HttpResponse("This is the login page for HealthTrack")