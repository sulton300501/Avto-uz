from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models.base import ActiveModel






class SiteSettings(ActiveModel):
    key = models.CharField(max_length=500 )
    value = models.TextField()



    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")
        ordering = ("key",)
    
    def __str__(self):
        return self.key
    




