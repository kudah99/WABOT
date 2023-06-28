from django.contrib import admin
from .models import FAQ
from import_export.admin import ImportExportMixin

class FAQAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display =("faq_question","answer")

admin.site.register(FAQ,FAQAdmin)