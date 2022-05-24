from django.contrib import admin
from content.models import Module, Cour, Td,  Tp,  homework, announcement

# Register your models here.

admin.site.register(Module)
admin.site.register(Cour)
admin.site.register(Td)
admin.site.register(Tp)
admin.site.register(homework)
admin.site.register(announcement)
