from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sur_name', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'sur_name')
    list_display_links = ('first_name', 'last_name', 'sur_name')
    prepopulated_fields = {'slug': ('last_name', 'first_name')}

@admin.register(EchoExamination)
class EchoExaminationAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'full_name', 'date_of_the_exam')