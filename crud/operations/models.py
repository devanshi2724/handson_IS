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
    components = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    user_id = models.IntegerField()
    customer_count = models.CharField(max_length=30)
    sti_owner = models.CharField(max_length=50)
    revenue = models.IntegerField(null=True, blank=True)
    effort_involved = models.IntegerField()
    no_of_customer = models.IntegerField()
    is_new_business = models.BooleanField(default=False, null=True, blank=True)
    creation_date = models.DateField()
    # last_updated = models.DateField(default=timezone.now) # New field for time trackin/g
    ideation_count = models.IntegerField(default=0)
    incubation_count = models.IntegerField(default=0)
    scaling_count = models.IntegerField(default=0)
    industrialized_count = models.IntegerField(default=0)
    optimised_count = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self) -> str:
        return self.project_name


