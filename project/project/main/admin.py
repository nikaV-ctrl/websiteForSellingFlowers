from django.contrib import admin

from .models import *

class Plants_admin(admin.ModelAdmin):
   list_display = ('title', 'img', 'price', 'description', 'light', 'availability')

class ForPlants_admin(admin.ModelAdmin):
   list_display = ('title', 'img', 'price', 'description', 'volume', 'availability')

class OceanTheme_admin(admin.ModelAdmin):
   list_display = ('title', 'img', 'price', 'description', 'availability')

admin.site.register(Plants, Plants_admin)
admin.site.register(ForPlants, ForPlants_admin)
admin.site.register(OceanTheme, OceanTheme_admin)