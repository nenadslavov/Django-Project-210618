from django.contrib import admin
from .models import Kategorija, Ploca


@admin.register(Kategorija)
class KategorijeAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}


@admin.register(Ploca)
class PloceAdmin(admin.ModelAdmin):
    list_display = ['album', 'autor', 'slug', 'cena',
                    'na_stanju', 'kreirana', 'azurirana']
    list_filter = ['na_stanju', 'kreirana', 'azurirana']
    list_editable = ['cena', 'na_stanju']
    prepopulated_fields = {'slug': ('album',)}
