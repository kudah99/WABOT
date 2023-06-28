from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ResponseMessagesForm,ResponseMessages
from import_export.admin import ImportExportMixin

class ResponseMessagesAdmin(ImportExportMixin, ModelAdmin):
    list_display =(
        "id",
        "sh_text",
        "nd_text",
        "en_text"
    )
    
    form =ResponseMessagesForm

admin.site.register(ResponseMessages,ResponseMessagesAdmin)
