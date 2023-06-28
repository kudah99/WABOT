from django.db import models

class Political_Parties(models.Model):
    name= models.CharField(max_length=50)
    logo= models.URLField(max_length=100)
    statement=models.CharField(max_length=300)