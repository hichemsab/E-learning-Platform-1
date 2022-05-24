from turtle import ondrag, title
from django.db import models





# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    coeffcient = models.IntegerField(null=False, blank=False)
    credit = models.IntegerField(null=False, blank=False)
    Speciality = models.ForeignKey("accounts.Speciality", on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

class Cour(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    cour = models.FileField(upload_to='Cour')
    module = models.ForeignKey(Module, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title

class Td(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    td = models.FileField(upload_to='TD', blank=True, null=True)
    module = models.ForeignKey(Module, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title

class Tp(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    tp = models.FileField(upload_to='TP')
    module = models.ForeignKey(Module, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title


class homework(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    quizz = models.FileField(upload_to='homework')
    module = models.ForeignKey(Module, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title

class correction(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    correction = models.FileField(upload_to='correction')
    module = models.ForeignKey(Module, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title

class announcement(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    announcement = models.FileField(upload_to='announcement')
    speciality = models.ForeignKey("accounts.Speciality", null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title