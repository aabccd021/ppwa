from django.urls import path

from . import views

urlpatterns = [
	path('hobby/',views.hobby, name='hobby'),
	path('register/',views.register, name='register'),
	path('jadwal/',views.jadwal, name='jadwal'),
	path('jadwal-baru/',views.new_schedule, name='new-schedule'),
	path('berhasil-jadwal/',views.schedule_post, name='success'),
	path('hapus-jadwal/',views.schedule_delete, name='schedule-delete'),
	path('aren/',views.aren, name='aren'),
	path('aren-hasil/',views.aren_hasil, name='aren-hasil'),
	path('sl/',views.sl, name='sl'),
	path('',views.index, name='index'),
]
