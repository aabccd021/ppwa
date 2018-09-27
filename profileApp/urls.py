from django.urls import path

from . import views

urlpatterns = [
	path('hobby/',views.hobby, name='hobby'),
	path('register/',views.register, name='register'),
	path('',views.index, name='index'),
]