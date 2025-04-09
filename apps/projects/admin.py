from django.contrib import admin
from .models import *





@admin.register(Comparisons)
class ComporisonAdmin(admin.ModelAdmin):
    model = Comparisons
    list_display = ("user_id","car_id")
    ordering = ("id",)




@admin.register(Favorites)
class FavouritesAdmin(admin.ModelAdmin):
    model = Favorites
    list_display = ("user","car","created_at")
    ordering = ("id",)





@admin.register(InspectionPlace)
class InspectionPlaceAdmin(admin.ModelAdmin):
    model = Favorites
    list_display = ("region","district")
    ordering = ("id",)
    




