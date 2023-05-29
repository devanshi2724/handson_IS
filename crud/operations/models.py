from time import timezone
from django import forms
from django.db import models


# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    
class IncubatorDB(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.TextField()
    no_of_employees = models.IntegerField()
   
    status = models.CharField(default=False, null=True, blank=True)
    user_id = models.IntegerField()
    
    sti_owner = models.CharField(max_length=50)
    revenue = models.IntegerField(null=True, blank=True)
    effort_involved = models.IntegerField()
    no_of_customer = models.IntegerField()
    is_new_business = models.BooleanField(default=False, null=True, blank=True)
    creation_date = models.DateField()
    # last_updated = models.DateField(default=timezone.now) # New field for time trackin/g
    # ideation_count = models.IntegerField(default=0)
    # incubation_count = models.IntegerField(default=0)
    # scaling_count = models.IntegerField(default=0)
    # industrialized_count = models.IntegerField(default=0)
    # optimised_count = models.IntegerField(default=0)
    # last_name = models.CharField(max_length=50, blank=True, null=True)
   
    STATUS_CHOICES = (
        ('ok', 'OK'),
        ('delayed', 'Delayed'),
        ('warning', 'Warning'),
        ('stopped', 'Stopped'),
    ) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    COMPONENT_CHOICES = [
        ["ideation", "Ideation"],
        ["incubation", "Incubation"],
        ["scaling", "Scaling"],
        ["industrialized", "Industrialized"],
        ["optimised", "Optimised"],
    ]
    
    components = models.CharField(max_length=100,choices=COMPONENT_CHOICES)
    TYPE_CHOICES = (
        ("evolution_platform", "Evolution Platform"),
        ("smart_industries", "Smart Industries"),
        ("augmented_customer_exp", "Augmented Customer Experience"),
        ("workplace_together", "Workplace Together"),
        ("impactful_data", "Impactful Data"),
        ("tools_for_ops", "Tools for Operations"),
    )
    type = models.CharField(max_length=50,choices=TYPE_CHOICES)
    CUSTOMER_CHOICES = ( ("mvp_poc", "MVP/POC"), ("pilot", "PILOT"), ("2-8_customers", "2-8 Customers"), ("8+_customers", "8+ Customers"), )
    customer_count = models.CharField(max_length=30,choices=CUSTOMER_CHOICES)


    def __str__(self) -> str:
        return self.project_name


