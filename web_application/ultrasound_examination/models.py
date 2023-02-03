from django.db import models
from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField('Имя', max_length = 50)
    last_name = models.CharField('Фамилия', max_length = 50)
    sur_name = models.CharField('Очество', max_length = 50, blank = True, null = True)
    date_of_birth = models.DateField('Дата рождения')

    height = models.IntegerField('Рост в см')
    weight = models.FloatField('Вес в кг')
    bsa = models.IntegerField()

    slug = models.SlugField('URL', max_length = 250, unique = True, db_index = True)

    def __str__(self):
        return f'{self.first_name}'

    def get_absolute_url(self):
        return reverse('patient_view', kwargs={'slug': self.slug, 'id': self.pk})

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        db_table = 'patients'
        ordering = ["first_name"]

class EchoExamination(models.Model):

    exams = models.ForeignKey('Patient', on_delete = models.PROTECT, null = True, verbose_name = 'Пациент')

    exam_name = models.CharField('Тип осмотра', max_length = 50, default = 'ЭхоКГ')
    date_of_the_exam = models.DateField('Дата осмотра', blank = True, null = True)
    RVWTd = models.FloatField('Толщина стенки правого желудочка в диастолу мм', blank = True, null = True)
    RVOTprox = models.FloatField('Выносящий тракт правого желудочкамм проксимальный мм', blank = True, null = True)
    RVOTdistal = models.FloatField('Выносящий тракт правого желудочкамм дистальный мм', blank = True, null = True)
    MPAdiam = models.FloatField('Легочный ствол мм', blank = True, null = True)
    RPAdiam = models.FloatField('Правая легочная артерия мм', blank = True, null = True)
    LPAdiam = models.FloatField('Левая легочная артерия мм', blank = True, null = True)

    IVSd = models.FloatField('Межжелудочковая перегородка в диастолу мм', blank = True, null = True)
    LVIDd = models.FloatField('Внутренний диаметр левого желудочка в диастолу мм', blank = True, null = True)
    LVIDs = models.FloatField('Внутренний диаметр левого желудочка в систолу мм', blank = True, null = True)
    LVPWd = models.FloatField('Нижне-боковая стенка левого желудочка мм', blank = True, null = True)
    LA_diam = models.FloatField('Левое предсердие в диастолу мм', blank = True, null = True)

    LVOTdiam = models.FloatField('Выносящий тракт левого желудочка мм', blank = True, null = True)
    AoAnnulus = models.FloatField('Аорта кольцо мм', blank = True, null = True)
    AoSinus = models.FloatField('Аорта синус мм', blank = True, null = True)
    Sinotubular_junction = models.FloatField('Аорта синотубулярное соединение мм', blank = True, null = True)
    AoAsc_prox = models.FloatField('Аорта восходящая часть проксимальная мм', blank = True, null = True)

    def __str__(self):
        return f'{self.exam_name}'
    def full_name(self):
        return f'{self.exams.first_name} {self.exams.last_name} {self.exams.sur_name}'
    def get_absolute_url(self):
        return reverse('exams', kwargs={'exam_name': self.exam_name})

    class Meta:
        verbose_name = 'Результат ЭхоКГ исследования'
        verbose_name_plural = 'Результаты ЭхоКГ исследования'
        db_table = 'exams'
        ordering = ["exam_name"]
