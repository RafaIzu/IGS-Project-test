from django.db import models

# Create your models here.

class Department(models.Model):
    depatName = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.depatName


class Employee(models.Model):
    Empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    depat = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Empname