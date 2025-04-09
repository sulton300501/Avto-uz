from django.db import  models
from django.utils.translation import gettext_lazy as _
from .fields import ActiveField
from .managers import ActiveManager
from django.template.defaultfilters import slugify
from django.utils.translation import get_language
from unidecode import unidecode
from django.conf import settings




class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Kiritilgan sana") , auto_now_add=True)
    updated_at = models.DateField(_("o'zgartrilgan sana"), auto_now=True)

    class Meta:
        abstract = True





class ActiveModel(models.Model):
    objects = ActiveManager()
    active = ActiveField()

    class Meta:
        abstract = True
    



class Slugify(models.Model):
    slug = models.SlugField(_("slug") , max_length=255 , unique=True , null=True , blank=True)
    SLUG_FROM_FIELD = None

    class Meta:
        abstract = True

    def _make_slug(self , value):
        if value is not None:
            original_slug = slugify(unidecode(value))
            unique_slug = original_slug
            num = 1
            while self.__class__.objects.exclude(pk=self.pk).filter(slug=unique_slug).exists():
                unique_slug = f"{original_slug}-{num}"
                num+=1
                
            return slugify(unique_slug)
        
    def save(self , *args , **kwargs):
        if self.slug is None:
            value_for_slug = getattr(self , self.SLUG_FROM_FIELD)
            self.slug = self._make_slug(value_for_slug)
        return super().save(*args , **kwargs)
    



class MultiLangSlugify(Slugify):
    slug_from_lang = models.CharField(
        choices=settings.MODELTRANSLATION_LANGUAGES_CHOICES,
        max_length=64,
        verbose_name=_("slug tilini tanlang"),
        null=True ,
        blank=True
    )

    class Meta:
        abstract = True

    
    def save(self, *args, **kwargs):
        if self.slug_from_lang is not None:
            value_for_slug = getattr(self , f"{self.SLOG_FROM_FIELD}_{self.slug_from_lang}")
            self.slug = self._make_slug(value_for_slug)

        if self.slug is None and self.slug_from_lang is None:
            self.slug_from_lang = get_language()
        return super().save(*args,**kwargs)



