from django.contrib import admin

from .models import MainMenu
from import_export.admin import ImportExportMixin

class mainMenu(ImportExportMixin,admin.ModelAdmin):
    list_display =(
        "feature_en",
        "feature_sh",
        "feature_nd",
        "slug",
        "last_updated",

    )

admin.site.register(MainMenu,mainMenu)
