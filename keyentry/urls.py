from django.urls import path

from . import models, forms, views


app_name = 'keyentry'


urlpatterns = [
    path('', views.keyentry, name='keyentry'),
    path('hourly/', views.form_hourly, name='form_hourly'),
    path('daily2/', views.form_daily2, name='form_daily2'),
    path('monthly/', views.form_monthly, name='form_monthly'),
]
