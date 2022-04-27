from re import M
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import UserManager
from content.models import Module


# Create your models here.



class Year(models.Model):
    YEARS = (
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    )
    year = models.CharField(max_length=2, choices=YEARS, default='L1', null=False, blank=False)
    def __str__(self):
        return self.year

class Speciality(models.Model):
    SPECIALITY = (
        ('MI', 'MI'),
        ('INFO', 'INFO'),
        ('MATH', 'MATH'),
        ('SI', 'SI'),
        ('ISIL', 'ISIL'),
        ('MATH', 'MATH'),
        ('STW', 'STW'),
        ('GLSD', 'GLSD'),
        ('MATHAPPLQ', 'MATHAPPLQ'),
        ('STW', 'STW'),
        ('GLSD', 'GLSD'),
        ('MATHAPPLQ', 'MATHAPPLQ'),
    )
        
    speciality = models.CharField(max_length=10, choices=SPECIALITY, default='MI', null=False, blank=False)
    year = models.ForeignKey(Year,null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return "{} - {}" .format(self.speciality, self.year)
      





class User(AbstractUser):
    GENDER = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    )
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, default='M', null=False, blank=False)
    

class Professor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, related_name='Professor')
    modules = models.ManyToManyField(Module)

    

    def __str__(self):
        return self.user.username

class Student(models.Model):                                                                                                                                                                                        
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    speciality = models.ForeignKey(Speciality,null=False, on_delete= models.CASCADE)


    def __str__(self):
        return self.user.username

