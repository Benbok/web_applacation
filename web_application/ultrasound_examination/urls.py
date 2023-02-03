from django.urls import path
from .views import *

# app_name = 'ultrasound_examination'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('patients/', patients, name='patients'),
    path('patients/<int:id>_<slug:slug>/', patient_view, name='patient_view'),
    path('exams/', echo, name='echo'),
]