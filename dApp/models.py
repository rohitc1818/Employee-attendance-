from django.db import models

# Create your models here.
class Employee(models.Model):
    E_no = models.IntegerField()
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=20)
    E_salary = models.FloatField()
    Contact_no = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Country = models.CharField(max_length=20)
    City = models.CharField(max_length=30)
    Pin_code = models.IntegerField()
    Address = models.CharField(max_length=150)

class Attendance(models.Model):
    E_no = models.IntegerField()
    E_name=models.CharField(max_length=30)
    In_date = models.IntegerField()
    Out_date = models.IntegerField()
    Description = models.CharField(max_length=120)

