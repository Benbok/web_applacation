from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'date_of_birth')

@admin.register(EchoExamination)
class EchoExaminationAdmin(admin.ModelAdmin):
    list_display = ('echo_exam', 'exam_name')