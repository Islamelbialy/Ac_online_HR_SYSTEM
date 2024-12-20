from django.db import models
from django.utils import timezone

# Create your models here.
class Branches(models.Model):
    name = models.CharField(null=False,unique=True,max_length=50,blank=False)
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=50, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(null=False,unique=True,max_length=50,blank=False,help_text="name can't be more than 50 character")
    description = models.TextField(null=False,max_length=255)
    phone = models.CharField(max_length=50, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    branche = models.ForeignKey('Branches',related_name="Branche_Department",on_delete= models.CASCADE)

    def __str__(self):
        return self.name