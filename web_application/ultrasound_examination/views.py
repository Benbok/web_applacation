from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'ultrasound_examination/base.html')
