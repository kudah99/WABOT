from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Political_Parties
from import_export.admin import ImportExportMixin

class PoliticalPartiesAdmin(ImportExportMixin, ModelAdmin):
    list_display = ('name', 'logo', 'statement')
    search_fields = ('name',)

admin.site.register(Political_Parties, PoliticalPartiesAdmin)