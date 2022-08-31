from django.contrib import admin

# Register your models here.
from .models import Student, Subject
# Register your models here.
@admin.register(Student)
class StuAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'roll', 'class_name', 'regi_no' ]

@admin.register(Subject)
class SbAdmin(admin.ModelAdmin):
    list_display = ['std', 'gpa', 'sub_name_1', 'sub_number1','sub_name_2', 'sub_number2','sub_name_3', 'sub_number3' ]
