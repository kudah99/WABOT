from django.db import models

class Constituency(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name