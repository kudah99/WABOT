from django.db import models

class Trivia(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=5, choices=[('true', 'True'), ('false', 'False')])

    def __str__(self):
        return self.question