
# Register your models here.
from django_neomodel import admin as neo_admin
from django.contrib import admin as dj_admin

from .models import Verse,Keyword
#  from .address import Address
#  from .intermediary import Intermediary
#  from .officer import Officer
#  from .other import Other

class VerseAdmin(dj_admin.ModelAdmin):
    list_display = ("name","text")
neo_admin.register(Verse, VerseAdmin)

class KeywordAdmin(dj_admin.ModelAdmin):
    list_display = ("name",)
neo_admin.register(Keyword, KeywordAdmin)

# class PersonAdmin(dj_admin.ModelAdmin):
#     list_display = ('name',)

# neo_admin.register(Person, PersonAdmin)