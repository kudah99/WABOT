from django.contrib import admin
from .models import Trivia
from import_export.admin import ImportExportMixin

class trivia(ImportExportMixin,admin.ModelAdmin):
    list_display =(
        "id",
        "question",
        "answer"
    )
    list_filter = ["id"]
admin.site.register(Trivia,trivia)