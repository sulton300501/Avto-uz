from modeltranslation.translator import TranslationOptions , register

from apps.common.models.model import SiteSettings

@register(SiteSettings)
class SiteSettingsTranslation(TranslationOptions):
    fields = (
        "key",
        "value",
    )


