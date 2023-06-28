from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Trivia
from import_export.admin import ImportExportMixin

class trivia(ImportExportMixin,ModelAdmin):
    list_display =(
        "id",
        "question",
        "answer"
    )
    list_filter = ["id"]
admin.site.register(Trivia,trivia)