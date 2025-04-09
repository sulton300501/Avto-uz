from django.db.models import CharField , BooleanField
from django.utils.translation import gettext_lazy as _
from apps.common.validator import phone_validator



class PhoneField(CharField):
    def __init__(self, verbose_name=_("Telefon raqam"),max_length=15 , validators=None , **kwargs):
        if validators is None:
            validators = [phone_validator]
        super().__init__(verbose_name=verbose_name,max_length=max_length , validators=validators, **kwargs)



class ActiveField(BooleanField):
    def __init__(self, verbose_name=_("active"), default=False, **kwargs):
        super().__init__(verbose_name=verbose_name , default=default , **kwargs)