from django.contrib import admin
from accounts.models import User, Professor, Student, Speciality
from django.contrib.auth.admin import UserAdmin 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Speciality)
