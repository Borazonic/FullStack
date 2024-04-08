from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    RollNo = models.IntegerField(default=0)
    Name = models.CharField(max_length=100,default='')
    DateOfBirth = models.DateField(default=datetime.now)
    DateOfAdmission = models.DateField(default=datetime.now)
    DateOfGraduation = models.DateField(default=datetime.now)
    Department = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.Name

class Teacher(models.Model):
    UID = models.IntegerField(default=0)
    Name = models.CharField(max_length=100,default='')
    DateOfBirth = models.DateField(default=datetime.now)
    DateOfJoining = models.DateField(default=datetime.now)
    Department = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.Name


class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    UID = models.IntegerField(default=0)
    Name = models.CharField(max_length=100,default='')
    DateOfBirth = models.DateField(default=datetime.now)
    DateOfJoining = models.DateField(default=datetime.now)
    def __str__(self):
        return self.Name

class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    def __str__(self):
        return f"{self.student} - {self.teacher}"