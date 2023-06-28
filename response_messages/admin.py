from django.contrib import admin

from .models import ResponseMessagesForm,ResponseMessages
from import_export.admin import ImportExportMixin

class ResponseMessagesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display =(
        "id",
        "sh_text",
        "nd_text",
        "en_text"
    )
    
    form =ResponseMessagesForm

admin.site.register(ResponseMessages,ResponseMessagesAdmin)
