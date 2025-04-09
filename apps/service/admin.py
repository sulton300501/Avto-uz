from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(ServiceDealer)
class ServiceDealerAdmin(admin.ModelAdmin):
    model = ServiceDealer
    list_display = ("name","address","phone_number")
    ordering = ("id",)
    




