from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Constituency
from import_export.admin import ImportExportMixin

@admin.register(Constituency)
class ConstituencyAdmin(ImportExportMixin,ModelAdmin):
    list_display = ['name', 'id']