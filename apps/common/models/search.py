from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.main.models import Announcement
from django.utils.translation import gettext_lazy as _





class ObjTypes(models.TextChoices):
    announcement = "announcement", _("Elonklar")


class SearchModel(models.Model):
    obj_type = models.CharField(max_length=255 , choices=ObjTypes.choices)
    user= models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE)
    announcement = models.ForeignKey("main.Announcement" , null=True , blank=True, on_delete=models.CASCADE )

    created_at = models.DateTimeField(null=True , blank=True)


    def __str__(self):
        return "Global Search"



@receiver(post_save , sender=Announcement)
def announcement_post_save(sender , instance , **kwargs):
    search  = SearchModel.objects.get_or_create(obj_type=ObjTypes.announcement , announcement=instance)
    search[0].created_at = instance.created_at
    search[0].save()
    

