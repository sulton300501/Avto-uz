from django.db import models
from apps.common.models.base import BaseModel
from django.utils.translation import gettext_lazy as _
from apps.common.models.base import MultiLangSlugify
# Create your models here.


class Reels(BaseModel):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE , related_name="reals")
    announcement = models.ForeignKey("main.Announcement",on_delete=models.CASCADE, related_name="announ_reel")
    entities_id = models.BigIntegerField(null=True , blank=True)  # model nomi (post , story)
    video_url = models.URLField(_("video"))
    caption = models.TextField(_("Foydalanuvchi commenti"))  # foydalanuvchi tomonidan comment
    likes = models.BigIntegerField(_("Likes"), default=0)
    view_count = models.BigIntegerField(_("Ko'rishlar soni"), default=0) # nechta foydalanuvchi tomosha qilganini saqlidi 
    


