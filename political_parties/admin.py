from django.contrib import admin
from .models import Political_Parties

class PoliticalPartiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'statement')
    search_fields = ('name',)

admin.site.register(Political_Parties, PoliticalPartiesAdmin)