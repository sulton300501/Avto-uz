from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.



    


class Comparisons(models.Model):   # yani bir nechta moshina tanlaydi va taqqoslaydi
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE , related_name="comparison" ,  verbose_name=_("Foydalanuvchi"))
    car_id = models.ForeignKey("main.Announcement", on_delete=models.CASCADE , related_name="comparisons", verbose_name=_("Taqqoslanayotgan avtomobil"))

    class Meta:
        verbose_name = _("Taqqoslash")
        verbose_name_plural = _("Taqqoslashlar")

    def __str__(self):
        return f"{self.user_id} - {self.car_id}"




class Favorites(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="favourites", verbose_name=_("Foydalanuvchi"))
    car = models.ForeignKey('main.Announcement', on_delete=models.CASCADE, related_name="favourites_cars",verbose_name=_("Sevimli avtomobil"))
    created_at = models.DateTimeField(auto_now_add=True , verbose_name=_("Yaratilgan vaqt"))


    class Meta:
        verbose_name = _("Sevimli")
        verbose_name_plural = _("Sevimlilar")

    def __str__(self):
        return f"{self.user} - {self.car}"



class InspectionPlace(models.Model):  # texnik ko'rikdan o'tkazilidigan joy
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

    region = models.CharField(_("Viloyat"), max_length=255, choices=RegionChoices.choices)
    district = models.CharField(_("Tuman"), max_length=255)

    class Meta:
        verbose_name = _("Texnik ko‘rik joyi")
        verbose_name_plural = _("Texnik ko‘rik joylari")

    def __str__(self):
        return f"{self.region} - {self.district}"




