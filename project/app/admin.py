from django.contrib import admin
from .models import *
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Recipe._meta.fields]
admin.site.register(Recipe, RecipeAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Ingredient._meta.fields]
admin.site.register(Ingredient, IngredientAdmin)

class IngredientItemAdmin(admin.ModelAdmin):
    list_display = [i.name for i in IngredientItem._meta.fields]
admin.site.register(IngredientItem, IngredientItemAdmin)
