from django.urls import path

from . import views

urlpatterns = [
	path('hobby/',views.hobby, name='hobby'),
	path('register/',views.register, name='register'),
	path('jadwal/',views.jadwal, name='jadwal'),
	path('jadwal-baru/',views.new_schedule, name='new-schedule'),
	path('berhasil-jadwal/',views.schedule_post, name='success'),
	path('',views.index, name='index'),
]
