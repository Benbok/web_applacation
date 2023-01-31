from django.db import models
from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()

    height = models.IntegerField('Рост в см')
    weight = models.FloatField('Вес в кг')
    bsa = models.IntegerField()

    def __str__(self):
        return f'{self.first_name}'

    def get_absolute_url(self):
        return reverse('patient_view', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        db_table = 'patients'
        ordering = ["-first_name"]

class EchoExamination(models.Model):
    echo_exam = models.ForeignKey('Patient', on_delete = models.PROTECT, null = True)
    exam_name = models.CharField('Тип исследования', default = 'ЭхоКГ исследование', max_length = 50)
    date_of_the_exam = models.DateField()
    RVWTd = models.FloatField('Толщина стенки правого желудочка в диастолу мм', default = 0)
    RVOTprox = models.FloatField('Выносящий тракт правого желудочкамм проксимальный мм', default = 0)
    RVOTdistal = models.FloatField('Выносящий тракт правого желудочкамм дистальный мм', default = 0)
    MPAdiam = models.FloatField('Легочный ствол мм', default = 0)
    RPAdiam = models.FloatField('Правая легочная артерия мм', default = 0)
    LPAdiam = models.FloatField('Левая легочная артерия мм', default = 0)

    IVSd = models.FloatField('Межжелудочковая перегородка в диастолу мм', default = 0)
    LVIDd = models.FloatField('Внутренний диаметр левого желудочка в диастолу мм', default = 0)
    LVIDs = models.FloatField('Внутренний диаметр левого желудочка в систолу мм', default = 0)
    LVPWd = models.FloatField('Нижне-боковая стенка левого желудочка мм', default = 0)
    LA_diam = models.FloatField('Левое предсердие в диастолу мм', default = 0)

    LVOTdiam = models.FloatField('Выносящий тракт левого желудочка мм', default = 0)
    AoAnnulus = models.FloatField('Аорта кольцо мм', default = 0)
    AoSinus = models.FloatField('Аорта синус мм', default = 0)
    Sinotubular_junction = models.FloatField('Аорта синотубулярное соединение мм', default = 0)
    AoAsc_prox = models.FloatField('Аорта восходящая часть проксимальная мм', default = 0)

    def __str__(self):
        return f'{self.exam_name}'

    def get_absolute_url(self):
        return reverse('echo_exam', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Результат исследования ЭхоКГ'
        verbose_name_plural = 'Результаты исследования ЭхоКГ'
        db_table = 'echo_exam'
        ordering = ["date_of_the_exam"]
