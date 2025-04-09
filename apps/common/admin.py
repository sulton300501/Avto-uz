from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from apps.common.models.model import *
from django.utils.translation import gettext_lazy as _
from core.settings.base import MODELTRANSLATION_LANGUAGES

# Register your models here.




class LoginForm(AuthenticationForm):

    def __init__(self, request = ..., *args, **kwargs):
        super(LoginForm , self).__init__( *args, **kwargs)


# admin.site.login_form = LoginForm
# admin.site.login_template = "login.html"



@admin.register(SiteSettings)
class SiteSetting(admin.ModelAdmin):
    model = SiteSettings
    list_display = ("id","key","active")
    search_fields = ("key_uz", "key_ru")
    list_filter = ("active",)
    ordering = ("id",)
    list_display_links = ("id", "key")
    fieldsets = (
        (_("O'zbekcha uz") , {"fields":("key_uz",)} ),
        (_("O'zbekcha uz") , {"fields":("value_uz",)} ),
        (_("Ruscha ru"), {"fields":("key_ru",)}),
        (_("Ruscha ru"), {"fields":("value_ru",)}),
        (_("Qoshimcha") , {"fields":("active",)}),

    )

    def get_form(self, request, obj = None, change = False, **kwargs):
        form = super().get_form(request , obj ,change , **kwargs)
        for value in form.base_fields:
          
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    



