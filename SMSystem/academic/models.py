from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=60)
    roll = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=50)
    regi_no = models.IntegerField(unique=True)
class Subject(models.Model):
    std = models.ForeignKey(Student,on_delete=models.CASCADE)
    gpa = models.CharField(max_length=10,default='n/a')
    sub_name_1 = models.CharField(max_length=30,blank=True,null=True)
    sub_number1 = models.IntegerField(blank=True,null=True)
    sub_name_2 = models.CharField(max_length=30,blank=True,null=True)
    sub_number2 = models.IntegerField(blank=True,null=True)
    sub_name_3 = models.CharField(max_length=30,blank=True,null=True)
    sub_number3 = models.IntegerField(blank=True,null=True)