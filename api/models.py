from django.db import models

# Create your models here.

# createing company model

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type= models.CharField(max_length=100, choices=(('It','IT'),
                                                    ('Non IT','Non IT'),
                                                    ("mobile Phones", "mobile Phone")
                                                    ))
    
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name + " at "+self.location

    # Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50, choices=(
        ('Manager', "manager"),
        ('Software Developer', "Software Developer"),
        ('Project Leader', 'Project Leader')
    ))

    company=models.ForeignKey(Company, on_delete=models.CASCADE)
