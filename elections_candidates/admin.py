from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportMixin
# Register your models here.
from django.contrib import admin
from .models import MemberOfParliamentCandidates,PresidentialCandidates


class MemberOfParliamentCandidatesAdmin(ImportExportMixin, ModelAdmin):
    list_display= (
        "id",
        "name",
        "about",
        "political_party",
        "constituency"
    )


class PresidentialCandidatesAdmin(ImportExportMixin, ModelAdmin):
    list_display= (
        "id",
        "name",
        "about",
        "political_party"
    )  
admin.site.register(MemberOfParliamentCandidates,MemberOfParliamentCandidatesAdmin)
admin.site.register(PresidentialCandidates,PresidentialCandidatesAdmin)