from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models.fields import PhoneField
from apps.common.utils import generate_upload_path
from sorl.thumbnail import ImageField
from apps.common.helpers import get_long_lat
from django.conf import settings






class ServiceDealer(models.Model):
    class DealerType(models.TextChoices):
        CAR_DEALER = "Car_Dealer", _("Avtomobil dileri")

    class DealerSubTypes(models.TextChoices):
        NEW = "New", _("Yangi")
        USED = "Used", _("Ishlatilgan")

    type = models.CharField(_("Diler turi"), max_length=50, choices=DealerType.choices)
    dealer_sub_type = models.CharField(_("Diler qo'shimcha turi"), max_length=50, choices=DealerSubTypes.choices)
    name = models.CharField(_("Diler nomi"), max_length=255)
    address = models.TextField(_("Manzil"))
    phone_number = PhoneField(_("Telefon raqami"))
    working_hours = models.CharField(_("Ish soatlari"), max_length=255)
    number_of_cars = models.PositiveIntegerField(_("Moshina raqami"), default=0)
    logo = ImageField(
        upload_to=generate_upload_path,
        null=True,
        blank=True,
        verbose_name=_("Diler logotipi"),
    )
    location_url = models.URLField(max_length=300, verbose_name=_("joylashinuvi"), null=True , blank=True)
    latitude = models.FloatField(_("Kenglik") , blank=True , null=True)
    longitude = models.FloatField(_("Uzunlik") , null=True , blank=True)
    description = models.TextField(_("Tavsif"), blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.location_url:
            long_lat, status = get_long_lat(self.location_url)
            if status and "long" in long_lat and "lat" in long_lat:
                self.longitude = float(long_lat["long"])
                self.latitude = float(long_lat["lat"])
        super(ServiceDealer, self).save(*args, **kwargs)


    @property
    def get_logo(self):
        if self.logo:
            return f"{settings.HOST}{self.logo.url}"



    class Meta:
        verbose_name = _("Xizmat dileri")
        verbose_name_plural = _("Xizmat dilerlari")
        ordering = ("id",)

    def __str__(self):
        return self.name
