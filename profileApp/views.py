from django.http import HttpResponseRedirect
from django.shortcuts import render

from profileApp.models import Schedule
from .forms import JadwalForm

response = {}


def index(request):
    return render(request, 'profileApp/index.html', {})


def hobby(request):
    return render(request, 'profileApp/hobby.html', {})

def register(request):
    return render(request, 'profileApp/buku_tamu.html')

def new_schedule(request):
    form = JadwalForm()
    return render(request, 'profileApp/jadwal_baru.html', {'form': form})

def schedule_post(request):
    form = JadwalForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        response['hari'] = request.POST['hari']
        response['tanggal'] = request.POST['tanggal']
        response['jam'] = request.POST['jam']
        response['nama'] = request.POST['nama']
        response['tempat'] = request.POST['tempat']
        response['kategori'] = request.POST['kategori']
        schedule = Schedule(hari=response['hari'],
                            tanggal=response['tanggal'],
                            jam=response['jam'],
                            nama=response['nama'],
                            tempat=response['tempat'],
                            kategori=response['kategori'])
        schedule.save()
        html = 'profileApp/jadwal_berhasil.html'
        return render(request, html, response)
    else:
        return render(request, 'profileApp/standar.html', {'text':'input tidak valid'})

def jadwal(request):
    jadwals = Schedule.objects.all().values()
    response['jadwals'] = jadwals
    return render (request, 'profileApp/jadwal.html', response)

def schedule_delete(request):
    Schedule.objects.all().delete()
    return render(request, 'profileApp/standar.html', {'text':'semua jadwal berhasil dihapus'})
