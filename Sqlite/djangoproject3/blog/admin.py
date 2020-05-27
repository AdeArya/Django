from django.contrib import admin

from .models import ModelsListView

class IndexAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update',
    ]


admin.site.register(ModelsListView, IndexAdmin)