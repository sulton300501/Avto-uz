from modeltranslation.translator import TranslationOptions, register
from .models import *



@register(Announcement)
class AnnouncementTranslation(TranslationOptions):
    fields = (
        "brand",
        "model",
        "color",     
        "description",
        "generation",

        
    )


@register(Prices)
class PriceTranslation(TranslationOptions):
    fields = (
        "currency",
       
    )




@register(CarOption)
class PriceTranslation(TranslationOptions):
    fields = (
        "name",
    )





@register(BodyParts)
class BodyTranslationAdmin(TranslationOptions):
    fields = (
        "body_name",
    )



@register(BodyConditions)
class BodyConditionTranslationAdmin(TranslationOptions):
    fields = (
        "condition_name",
    )




