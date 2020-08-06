from django.db import models


# Create your models here.

class Employees(models.Model):
    GENDER_LIST = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(choices=GENDER_LIST, max_length=1)
    address = models.TextField()
    emp_job = models.ManyToManyField("AvailableJobs",blank=True)
    date_of_birth = models.DateField()
    
    class Meta:   
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.first_name

class AvailableJobs(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

