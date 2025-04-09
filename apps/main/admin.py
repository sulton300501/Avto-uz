from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
from core.settings.base import MODELTRANSLATION_LANGUAGES




@admin.register(Announcement)
class Announcements(admin.ModelAdmin):
    model = Announcement
    list_display = ("id","dealer_id","brand","model","year")
    search_fields = (
        "brand_uz", "brand_ru",
        "model_uz","model_ru",
        
        )
   
    ordering = ("id",)
    list_display_links = ("id", "dealer_id","brand")
  
    fieldsets = (
        (_("O'zbekcha uz"),{"fields":("brand_uz","model_uz","color_uz","description_uz","generation_uz")}),
          (_("Ruscha ru"),{"fields":("brand_ru","model_ru","color_ru","description_ru","generation_ru")}),
        (None , {
            "fields":( "user_id", "dealer_id",  "year", "price", "milage",
                "engine_capacity", "gearbox_type", "fuel_type", "gas_type",
                "description", "generation", "body_type", "power", "passport_type",
                "purchase_date", "ownership_type", "status", "is_daily_offer",
                "favorite_count", "inspection_place")
        }),
 
    
     

    )

    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    






@admin.register(Prices)
class Price(admin.ModelAdmin):
    model = Prices
    list_display = ("id","price","currency","discount")
    search_fields = (
        "currency_uz", "currency_ru",
   
        
        )
   
    ordering = ("id",)
    list_display_links = ("id", "price","currency")
  
    fieldsets = (
        (_("O'zbekcha uz"),{"fields":("currency_uz",)}),
          (_("Ruscha ru"),{"fields":("currency_ru",)}),
        (None , {
            "fields":( "car_id","price","discount")
        }),
 
    
     

    )

    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    







@admin.register(CarOption)
class CarOptionAdmin(admin.ModelAdmin):
    model = CarOption
    list_display = ("id","name")
    search_fields = (
        "name_uz", "name_ru",
   
        
        )
   
    ordering = ("id",)
    list_display_links = ("id", "name")
  
    fieldsets = (
        (_("O'zbekcha uz"),{"fields":("name_uz",)}),
          (_("Ruscha ru"),{"fields":("name_ru",)}),
      
    
     

    )

    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    









@admin.register(CarOptionsMapping)
class CarOptionMapping(admin.ModelAdmin):
  
    model = CarOptionsMapping
    list_display = ("id","car_id","car_options_id")
  
   
    ordering = ("id",)
    list_display_links = ("id", "car_id","car_options_id")

    fieldsets = (
        
        (None , {
            "fields":( "car_id","car_options_id")
        }),
    )



    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    
 




  
  







@admin.register(BodyConditions)
class BodyConditionAdmin(admin.ModelAdmin):
   
    model = BodyConditions
    list_display = ("id","condition_name")
  
   
    ordering = ("id",)
    list_display_links = ("id", "condition_name")

    fieldsets = (
        (_("O'zbekcha uz"),{"fields":("condition_name_uz",)}),
          (_("Ruscha ru"),{"fields":("condition_name_ru",)}),
   
      
    )



    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    
 




  
  



@admin.register(BodyParts)
class BodyPartsAdmin(admin.ModelAdmin):
    model = BodyParts
    list_display = ("id","body_name")
  
   
    ordering = ("id",)
    list_display_links = ("id", "body_name")

    fieldsets = (
        
        (_("O'zbekcha uz"),{"fields":("body_name_uz",)}),
        (_("Ruscha ru"),{"fields":("body_name_ru",)}),
    )



    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    
 





@admin.register(BodyStatus)
class BodyStatusAdmin(admin.ModelAdmin):
  
    model = BodyStatus
    list_display = ("id","car_id","body_part","condition")
  
   
    ordering = ("id",)
    list_display_links = ("id", "car_id","body_part","condition")




    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    
 




  
  


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    model = Images
    list_display = ("id","car_id","is_main")
  
   
    ordering = ("id",)
    list_display_links = ("id", "car_id")
    

    fieldsets = (
        (None, {
            "fields": (
                "car_id","image_url","is_main"
            ),
        }),
    )
    




    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    
 







