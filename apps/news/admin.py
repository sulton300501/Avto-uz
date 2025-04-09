from django.contrib import admin
from .models import *
from core.settings.base import MODELTRANSLATION_LANGUAGES
# Register your models here.

from django.utils.translation import gettext_lazy as _






@admin.register(Reels)
class BodyStatusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    model = Reels
    list_display = ("id","entities_id","likes")
  
   
    ordering = ("id",)
    list_display_links = ("id", "entities_id")

    fieldsets = (
        (_("O'zbekcha uz") , {"fields":("caption_uz",)} ),
    
        (_("Ruscha ru"), {"fields":("caption_ru",)}),
        (None , {"fields": ("user","announcement","entities_id","video_url","likes","view_count")})
     

    )


    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form