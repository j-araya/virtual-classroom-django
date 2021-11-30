from django.db import models

# Create your models here.

class Profesor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True)
    address = models.TextField(blank=True)
    date_init = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
        

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True)
    address = models.TextField(blank=True)
    date_init = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Subject(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, blank=True)
    profesor = models.ForeignKey(Profesor, models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)

class Unit(models.Model):
    name = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Class(models.Model):
    title = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, models.CASCADE)
    unit = models.ForeignKey(Unit, models.CASCADE)
    profesor = models.ForeignKey(Profesor, models.SET_NULL, null=True)
    video = models.URLField()
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)