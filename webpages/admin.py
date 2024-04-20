from django.contrib import admin
from .models import Student
from .models import Myuser
# Register your models here.
admin.site.register(Myuser)
admin.site.register(Student)