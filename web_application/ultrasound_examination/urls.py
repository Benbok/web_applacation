from django.urls import path
from .views import *

# app_name = 'ultrasound_examination'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('patients/', patients, name='patients'),
    path('patient_view/<int:id>/', patient_view, name='patient_view'),
    path('echo_exam/<int:id>/', echo_exam, name='echo_exam'),
]