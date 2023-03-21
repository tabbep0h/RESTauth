from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'


MARKS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    subjects = models.ManyToManyField(Subject)
    marks = models.CharField(choices=MARKS_CHOICES, max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Студенты'
        verbose_name = 'Студент'


class Grade(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Класс'
        verbose_name = 'Классы'

