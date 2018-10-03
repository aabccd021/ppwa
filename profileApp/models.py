from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)


class Schedule(models.Model):
    hari = models.CharField(max_length=10)
    tanggal = models.DateField()
    jam = models.TimeField()
    nama = models.CharField(max_length=30)
    tempat = models.CharField(max_length=30)
    kategori = models.CharField(max_length=15)
