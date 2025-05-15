from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Departament(models.Model):
    DEPARTAMENT_CHOICES = [
        ('Cистемного проектування', 'Cистемного проектування'),
        ('Радіофізики та комп’ютерних технологій', 'Радіофізики та комп’ютерних технологій'),
        ('Радіоелектронних і комп’ютерних систем', 'Радіоелектронних і комп’ютерних систем'),
        ('Оптоелектроніки та інформаційних технологій', 'Оптоелектроніки та інформаційних технологій'),
    ]
    departament = models.CharField(max_length=50, null=True, choices=DEPARTAMENT_CHOICES)

    def __str__(self):
        return self.departament if self.departament else "Без назви"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest, blank=True)
    departament = models.ForeignKey(Departament, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thesis_topic = models.CharField(max_length=200, null=True)
    full_name = models.CharField(max_length=100, null=True)
    course = models.IntegerField(null=True)
    assigned_slot = models.OneToOneField('Slot', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Slot(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(default=1)
    students = models.ManyToManyField(Student, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_full(self):
        return self.students.count() >= self.capacity

    def __str__(self):
        return f"{self.teacher.name} [{self.students.count()}/{self.capacity}]"

