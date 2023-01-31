from django.shortcuts import render, HttpResponse
from .models import *

def home_page(request):
    return render(request, 'ultrasound_examination/home_page.html')

def patients(request):
        patients = Patient.objects.all()
        # examination = Exception.objects.filter(cho_exam = patients.id)
        context = {'patients': patients}
        return render(request, 'ultrasound_examination/patients.html', context=context)

def patient_view(request, id):
    return HttpResponse(f"Осмотр № {id}")

def echo_exam(request, id):
    return HttpResponse(f"Эхо номер {id}")