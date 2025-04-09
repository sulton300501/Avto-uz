from django.shortcuts import render
from rest_framework import generics
from apps.common.models.model import SiteSettings
from .serializers import SiteSettingSerializer
# Create your views here.



class SiteSettingView(generics.ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingSerializer

    def get_queryset(self):
        return self.queryset.filter(active=True)