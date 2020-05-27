from django.contrib import admin
from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update',
    ]

admin.site.register(Artikel, ArtikelAdmin)