from django.http.response import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'authentication.html')


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'index.html')
 