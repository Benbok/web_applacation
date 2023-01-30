from django.urls import path
from .views import *

app_name = 'ultrasound_examination'

urlpatterns = [
    path('', index, name='index'),
]