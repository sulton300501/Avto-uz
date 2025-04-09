from django.db import models 
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField
from django.utils.translation import gettext_lazy as _
from apps.common.models.base import BaseModel
from apps.common.utils import generate_upload_path
from apps.common.models.fields import PhoneField
from django.conf import settings



class User(AbstractUser , BaseModel):
    class RegionChoices(models.TextChoices):
        TASHKENT = "Tashkent", _("Tashkent")
        SAMARKAND = "Samarkand", _("Samarkand")
        BUKHARA = "Bukhara", _("Bukhara")
        NAMANGAN = "Namangan", _("Namangan")
        ANDIJAN = "Andijan", _("Andijan")
        FERGANA = "Fergana", _("Fergana")
        NAVOIY = "Navoi", _("Navoi")
        SURKHANDARYA = "Surkhandarya", _("Surkhandarya")
        KASHKADARYA = "Kashkadarya", _("Kashkadarya")
        SIRDARYA = "Sirdarya", _("Sirdarya")
        KHOREZM = "Khorezm", _("Khorezm")
        JIZZAKH = "Jizzakh", _("Jizzakh")
        KARAKALPAKSTAN = "Karakalpakstan", _("Karakalpakstan")          
             

    full_name = models.CharField(_("F.I.Sh") , max_length=255 )
    profile_picture = ImageField(verbose_name=_("Foydlanuvchi rasmi"), upload_to=generate_upload_path)
    phone_number = PhoneField(verbose_name=_("Asosiy raqam"))
    is_dealer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True , blank=True)
    region = models.CharField(_("Yashash manzili"), choices=RegionChoices.choices , max_length=255)
    user_count_data = models.BigIntegerField(_("Foydalanuvchining malumotlar son"), default=0)


    @property
    def get_profile_image(self):
        if self.profile_picture:
            return f"{settings.HOST}{self.profile_picture.url}"
        
    
    class Meta:
        verbose_name = _("Foydalanuvchilar")
        verbose_name_plural = _("Foydalanuvchilar")

