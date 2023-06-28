from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MemberOfParliamentCandidates,PresidentialCandidates


class MemberOfParliamentCandidatesAdmin(admin.ModelAdmin):
    list_display= (
        "id",
        "name",
        "about",
        "political_party",
        "constituency"
    )


class PresidentialCandidatesAdmin(admin.ModelAdmin):
    list_display= (
        "id",
        "name",
        "about",
        "political_party"
    )  
admin.site.register(MemberOfParliamentCandidates,MemberOfParliamentCandidatesAdmin)
admin.site.register(PresidentialCandidates,PresidentialCandidatesAdmin)