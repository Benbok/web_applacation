from django import template
from ultrasound_examination.models import *

register = template.Library()

@register.simple_tag()
def get_all_patients():
    return Patient.objects.all()

@register.simple_tag()
def get_all_echo_exams():
    return EchoExamination.objects.all()