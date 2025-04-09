from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import truncatechars
from apps.common.models.base import BaseModel , MultiLangSlugify
from sorl.thumbnail import ImageField
from apps.common.utils import generate_upload_path

# Create your models here.


from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models.base import BaseModel

class Announcement(BaseModel , MultiLangSlugify):
    class GearboxType(models.TextChoices):
        AUTOMATIC = "Automatic", _("Automatic")
        MANUAL = "Manual", _("Manual")

    class FuelType(models.TextChoices):
        PETROL = "Petrol", _("Petrol")
        DIESEL = "Diesel", _("Diesel")
        ELECTRIC = "Electric", _("Electric")
        HYBRID = "Hybrid", _("Hybrid")

    class GasType(models.TextChoices):
        METHANE = "Methane", _("Methane")
        PROPANE = "Propane", _("Propane")
        BUTANE = "Butane", _("Butane")

    class BodyType(models.TextChoices):
        SEDAN = "Sedan", _("Sedan")
        COUPE = "Coupe", _("Coupe")

    class PassportType(models.TextChoices):
        LOCAL = "Local", _("Local")
        IMPORT = "Import", _("Import")

    class OwnershipType(models.TextChoices):
        INDIVIDUAL = "Individual", _("Individual")
        COMPANY = "Company", _("Company")
        RENTAL = "Rental", _("Rental")

    class StatusType(models.TextChoices):
        SOLD = "Sold", _("Sold")
        UNSOLD = "Unsold", _("Unsold")

    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="announcements")
    dealer_id = models.ForeignKey("service.ServiceDealer", on_delete=models.CASCADE, related_name="dealer_services")
    brand = models.CharField(_("Mashina brandi"), max_length=255)
    model = models.CharField(_("Moshina Model"), max_length=255)
    year = models.PositiveIntegerField(_("Ishlab chiqarilgan yil"))
    price = models.BigIntegerField(_("Mashina narxi"), default=0)
    milage = models.BigIntegerField(_("Yurgan masofa (km)"), default=0)
    color = models.CharField(_("Rang"), max_length=50)
    engine_capacity = models.PositiveIntegerField(_("Dvigatel hajmi (kub sm yoki litr)"), help_text="Enter in cc or liters")
    gearbox_type = models.CharField(_("Uzatmalar qutisi"), choices=GearboxType.choices, max_length=10)
    fuel_type = models.CharField(_("Yoqilg‘i turi"), choices=FuelType.choices, max_length=100)
    gas_type = models.CharField(_("Gaz turi"), choices=GasType.choices, max_length=100, blank=True, null=True)
    description = models.TextField(_("Tavsif"))
    generation = models.CharField(_("Avlod"), max_length=255, null=True, blank=True)
    body_type = models.CharField(_("Kuzov turi"), choices=BodyType.choices, max_length=100, null=True, blank=True)
    power = models.PositiveIntegerField(_("Ot kuchi"))
    passport_type = models.CharField(_("Pasport turi"), choices=PassportType.choices, max_length=100, null=True, blank=True)
    purchase_date = models.DateField(_("Xarid qilingan sana"), null=True, blank=True)
    ownership_type = models.CharField(_("Egalik turi"), choices=OwnershipType.choices, max_length=255, null=True, blank=True)
    status = models.CharField(_("Holat"), choices=StatusType.choices, max_length=100)
    is_daily_offer = models.BooleanField(_("Kunlik taklif"), default=False)
    favorite_count = models.PositiveIntegerField(_("Saqlanganlar soni"), default=0)
    inspection_place = models.ForeignKey("projects.InspectionPlace", on_delete=models.CASCADE , related_name="inspected_announcements")
    SLUG_FROM_FIELD = "model"

    
    @property
    def short_description_func(self):
        return truncatechars(self.description , 30)
    
    short_description_func.fget.short_description = _("Qisqacha sarlavha")
    

    class Meta:
        verbose_name = _("Elon")
        verbose_name_plural = _("1. Elonlar")
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"



class Prices(models.Model):   #  moshinaga chegirma berish uchun
    car_id = models.ForeignKey(Announcement,on_delete=models.CASCADE, verbose_name=_("Elonlar"), related_name="prices")
    price = models.BigIntegerField(_("Narxi"))
    currency = models.CharField(_("Valyuta turi"), max_length=50)
    discount = models.FloatField(_("chegirma %") , null=True , blank=True)

    class Meta:
        verbose_name = _("Narx")
        verbose_name_plural = _("2. Narxlar")
        ordering = ("price",)


    def __str__(self):
        return f"Narxlar {self.price}"





class CarOption(models.Model):
    name = models.CharField(_("Moshina opsiyalari"), max_length=255)

    class Meta:
        verbose_name = _("Optsiya nomi")
        verbose_name_plural = _("3. Optsiya nomlari")
        ordering = ("name",)


    def __str__(self):
        return self.name








class CarOptionsMapping(models.Model):
    car_id = models.ForeignKey(Announcement,on_delete=models.CASCADE, related_name="caroptionmapping")
    car_options_id = models.ForeignKey(CarOption , on_delete=models.CASCADE , related_name="car_option")

    class Meta:
        verbose_name = _("Mashina optsiyalar xaritasi")
        verbose_name_plural = _("4. Moshina optsiyalar xaritasi")


class BodyParts(models.Model):
    body_name = models.CharField(_("moshina tanasi"), max_length=255)

    class Meta:
        verbose_name = _("Moshina tanasi")
        verbose_name_plural = _("5. Moshina tanasi")

    def __str__(self):
        return self.body_name
       



class BodyConditions(models.Model):
    condition_name = models.CharField(_("Moshina xolati"), max_length=255)

    class Meta:
        verbose_name = _("Holati")
        verbose_name_plural = _("6. Holatlari")

    def __str__(self):
        return self.condition_name
       


class BodyStatus(models.Model):
    car_id = models.ForeignKey(Announcement ,verbose_name=("Elon") , on_delete=models.CASCADE , related_name="body_status")
    body_part = models.ForeignKey(BodyParts, verbose_name=("Moshina tanasi"), on_delete=models.CASCADE , related_name="bodypart")
    condition = models.ForeignKey(BodyConditions, verbose_name=("Moshina xolati"), on_delete=models.CASCADE,related_name="condition")

    class Meta:
        verbose_name = _("Tana qismlarining xolati")
        verbose_name_plural = _("7. Tana qismlarining xolati")

    
    def __str__(self):
        return f"{self.car_id} {self.body_part} {self.condition}"




class Images(models.Model):
    car_id = models.ForeignKey(Announcement , on_delete=models.CASCADE,related_name="images")
    image_url = ImageField(verbose_name=_("rasmlar") , upload_to=generate_upload_path)
    is_main = models.BooleanField(_("Asosiy rasm"))

    class Meta:
        verbose_name = _("Rasm")
        verbose_name_plural = _("8. Rasmlar")





















    








