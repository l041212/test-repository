from django.db import models

# Create your models here.

class User(models.Model):
    code=models.CharField(max_length=32,null=True)
    name=models.CharField(max_length=32,null=True)
    password=models.CharField(max_length=64,null=True)
    sex=models.CharField(max_length=4,null=True)
    company=models.CharField(max_length=128,null=True)