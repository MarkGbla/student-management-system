from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=25)
    program = models.CharField(max_length=25)
    level = models.CharField(max_length=50, default='Beginner')

    
    def __str__(self):
        return f'(first_name)'
    
    
    
