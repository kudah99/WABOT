from django.contrib import admin
from .models import FAQ
from import_export.admin import ImportExportMixin
from unfold.admin import ModelAdmin

class FAQAdmin(ImportExportMixin,ModelAdmin):
    list_display =("faq_question","answer")

admin.site.register(FAQ,FAQAdmin)