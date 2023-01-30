# Generated by Django 4.1.5 on 2023-01-28 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('height', models.IntegerField(verbose_name='Рост в см')),
                ('weight', models.FloatField(verbose_name='Вес в кг')),
                ('bsa', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
                'db_table': 'patients',
                'ordering': ['-first_name'],
            },
        ),
        migrations.CreateModel(
            name='EchoExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(default='ЭхоКГ исследование', max_length=50, verbose_name='Тип исследования')),
                ('date_of_the_exam', models.DateField()),
                ('RVWTd', models.FloatField(default=0, verbose_name='Толщина стенки правого желудочка в диастолу мм')),
                ('RVOTprox', models.FloatField(default=0, verbose_name='Выносящий тракт правого желудочкамм проксимальный мм')),
                ('RVOTdistal', models.FloatField(default=0, verbose_name='Выносящий тракт правого желудочкамм дистальный мм')),
                ('MPAdiam', models.FloatField(default=0, verbose_name='Легочный ствол мм')),
                ('RPAdiam', models.FloatField(default=0, verbose_name='Правая легочная артерия мм')),
                ('LPAdiam', models.FloatField(default=0, verbose_name='Левая легочная артерия мм')),
                ('IVSd', models.FloatField(default=0, verbose_name='Межжелудочковая перегородка в диастолу мм')),
                ('LVIDd', models.FloatField(default=0, verbose_name='Внутренний диаметр левого желудочка в диастолу мм')),
                ('LVIDs', models.FloatField(default=0, verbose_name='Внутренний диаметр левого желудочка в систолу мм')),
                ('LVPWd', models.FloatField(default=0, verbose_name='Нижне-боковая стенка левого желудочка мм')),
                ('LA_diam', models.FloatField(default=0, verbose_name='Левое предсердие в диастолу мм')),
                ('LVOTdiam', models.FloatField(default=0, verbose_name='Выносящий тракт левого желудочка мм')),
                ('AoAnnulus', models.FloatField(default=0, verbose_name='Аорта кольцо мм')),
                ('AoSinus', models.FloatField(default=0, verbose_name='Аорта синус мм')),
                ('Sinotubular_junction', models.FloatField(default=0, verbose_name='Аорта синотубулярное соединение мм')),
                ('AoAsc_prox', models.FloatField(default=0, verbose_name='Аорта восходящая часть проксимальная мм')),
                ('echo_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ultrasound_examination.patient')),
            ],
            options={
                'verbose_name': 'Результат исследования ЭхоКГ',
                'verbose_name_plural': 'Результаты исследования ЭхоКГ',
                'db_table': 'echo_exam',
                'ordering': ['date_of_the_exam'],
            },
        ),
    ]