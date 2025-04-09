from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from apps.users.models import *
from django.utils.translation import gettext_lazy as _
from core.settings.base import MODELTRANSLATION_LANGUAGES





@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("id","full_name","phone_number")
    search_fields = ("full_name", "phone_number")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "full_name","phone_number")
    fieldsets = (
        (_("O'zbekcha uz") , {"fields":("full_name_uz",)} ),
        (_("Ruscha ru"), {"fields":("full_name_ru",)}),
        (None , {"fields":("profile_picture","phone_number","is_dealer","is_active","is_staff","is_superuser","last_login","region","user_count_data")})
    
     

    )

    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    



