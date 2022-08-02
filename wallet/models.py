from tkinter import TRUE
from django.db import models
# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15,null=True)
    last_name = models.CharField(max_length=15,null=True)
    # gender = models.CharField(max_length=10,null=True)
    # address = models.TextField()
    # age = models.PositiveIntegerField()
    # nationality = models.CharField(max_length=15,null=True)
    # id_number = models.CharField(max_length=10,null=True)
    # phone_number = models.CharField(max_length=15,null=True)
    # email = models.EmailField()