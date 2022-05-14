from re import M
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.forms import ValidationError
from content.models import Module
from django.core.exceptions import ValidationError


# Create your models here.

class Speciality(models.Model):
    SPECIALITY = (
        ('MI - L1', 'MI - L1'),
        ('INFO - L2', 'INFO - L2'),
        ('MATH - L2', 'MATH - L2'),
        ('SI - L3', 'SI - L3'),
        ('ISIL - L3', 'ISIL - L3'),
        ('MATH - L3', 'MATH - L3'),
        ('STW - M1', 'STW - M1'),
        ('GLSD - M1', 'GLSD - M1'),
        ('MATHAPPLQ - M1', 'MATHAPPLQ - M1'),
        ('STW - M2', 'STW - M2'),
        ('GLSD - M2', 'GLSD - M2'),
        ('MATHAPPLQ - M2', 'MATHAPPLQ - M2'),
    )
        
    speciality = models.CharField(max_length=20, choices=SPECIALITY, default='MI', null=False, blank=False, unique=True)

    
    def __str__(self):
        return self.speciality





class User(AbstractUser):
    GENDER = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    )
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, default='M', null=True, blank=False)
    

class Professor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, related_name='Professor')
    modules = models.ManyToManyField(Module)

    def clean(self, *args, **kwargs):
        if self.modules.count() > 4:
            raise ValidationError("You can't assign more than three modules")
        super(Professor, self).clean(*args, **kwargs)
    

    def __str__(self):
        return self.user.username

class Student(models.Model):                                                                                                                                                                                        
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    speciality = models.ForeignKey(Speciality,null=False, on_delete= models.CASCADE)


    def __str__(self):
        return self.user.username

