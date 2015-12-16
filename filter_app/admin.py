from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
	exclude = ['slug', ]
	#pass

@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
	exclude = ['previous_filter',]

@admin.register(models.Chemistry)
class ChemistryAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Filter)
class FilterAdmin(admin.ModelAdmin):
	pass

@admin.register(models.FilterSwap)
class FilterSwapAdmin(admin.ModelAdmin):
	pass
