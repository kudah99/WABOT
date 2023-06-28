from django.contrib import admin

from .models import WAUsers
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class WAUsersAdmin(admin.ModelAdmin):
    list_display =(
        "id",
        "user_name",
        "phone_number",
        "IsRegistered",
        "IsBlocked",
        "createdAt",
    )
    list_filter = ["createdAt"]
    search_fields = ('phone_number__startswith',)

admin.site.register(WAUsers,WAUsersAdmin)