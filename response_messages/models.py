from django import forms
from django.db import models



class ResponseMessages(models.Model):
    sh_text = models.TextField( null=True)
    nd_text = models.TextField(null=True )
    en_text = models.TextField(null=True )

class ResponseMessagesForm(forms.ModelForm):
    class Meta:
        model = ResponseMessages
        fields = ('__all__')
