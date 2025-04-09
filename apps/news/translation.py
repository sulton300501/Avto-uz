from modeltranslation.translator import TranslationOptions, register
from .models import *




@register(Reels)
class ReelsTranslation(TranslationOptions):
    fields = (
        "caption", 
    )
