from django.db import models
from constituency.models import Constituency
from import_export.admin import ImportExportMixin


class MemberOfParliamentCandidates(ImportExportMixin,models.Model):
    name = models.CharField( max_length=50)
    about = models.CharField(max_length=300)
    political_party = models.CharField( max_length=50)
    constituency = models.ForeignKey(Constituency, verbose_name=("mp_constituency"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PresidentialCandidates(ImportExportMixin,models.Model):
    name = models.CharField( max_length=50)
    about = models.CharField(max_length=300)
    political_party= models.CharField(max_length=50)
    created_at = models.DateTimeField(  auto_now_add=True)