from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *

def home_page(request):
    return render(request, 'ultrasound_examination/home_page.html')

def patients(request):
        return render(request, 'ultrasound_examination/patients.html')

def patient_view(request, slug, id):
    patient = get_object_or_404(Patient, slug=slug)
    echo = EchoExamination.objects.filter(exams=id)
    count_echo = EchoExamination.objects.filter(exams = id).count()
    context = {'patient': patient,
               'echo': echo,
               'count_echo': count_echo}
    return render(request, 'ultrasound_examination/patient_view.html', context = context)



def echo(request):
    return render(request, 'ultrasound_examination/echo.html')
