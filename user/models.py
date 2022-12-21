from datetime import timedelta

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Язык программирования')
    month_to_learn = models.IntegerField(verbose_name='Продолжительность курса')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    email = models.CharField(max_length=50, unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number[:1] == '0':
            self.phone_number = self.phone_number.replace('0', '+996', 1)
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=50, null=True, verbose_name='Место учебы/работы')
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=50, verbose_name='Предпочитаемая ОС', choices=[])

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True, verbose_name='Основное место работы')
    experience = models.DateField(verbose_name='Дата начала работы')
    students = models.ManyToManyField(Student, related_name='mentors', through='Course')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование курса')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField(verbose_name='Дата начала курсов')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_end_date(self):
        pass
