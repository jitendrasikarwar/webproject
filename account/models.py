from django.db import models
# Create your models here.
class person(models.Model):
    user=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    password=models.IntegerField()