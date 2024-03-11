from django.db import models

class Item(models.Model):
    SL_no = models.AutoField(primary_key=True)
    ID = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=50)
    Group = models.CharField(max_length=50)
    Contact = models.CharField(max_length=20)
    Active = models.BooleanField(default=True) 

