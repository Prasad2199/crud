from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures/%y/%m/%d/',max_length=255,null=True,blank=True)
    summary = models.CharField(max_length=500)