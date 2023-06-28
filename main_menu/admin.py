from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import MainMenu
from import_export.admin import ImportExportMixin

class mainMenu(ImportExportMixin,ModelAdmin):
    list_display =(
        "feature_en",
        "feature_sh",
        "feature_nd",
        "slug",
        "last_updated",

    )

admin.site.register(MainMenu,mainMenu)
