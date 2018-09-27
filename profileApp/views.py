from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'profileApp/index.html', {})

def hobby(request):
    return render(request, 'profileApp/hobby.html', {})

def register(request):
    return render(request, 'profileApp/buku_tamu.html', {})