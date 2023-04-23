from django.contrib import admin
from .models import Details

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('year', 'branch', 'placed', 'placed_on', 'package')
admin.site.register(Details, DetailsAdmin)