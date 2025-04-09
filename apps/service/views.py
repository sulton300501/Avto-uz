from django.shortcuts import render
from .models import *
from apps.service import serializers
from rest_framework import generics
from rest_framework.parsers import FormParser , MultiPartParser



class ServiceDealerView(generics.CreateAPIView):
    parser_classes = (FormParser , MultiPartParser)
    queryset = ServiceDealer.objects.all()
    serializer_class = serializers.ServiceDealerSerializer
    



class ServiceDealerAllView(generics.ListAPIView):
    queryset = ServiceDealer.objects.all()
    serializer_class = serializers.ServiceDealerAllSerializer

    def get_queryset(self):
        return self.queryset.filter()




class ServiceDealerDeleteView(generics.DestroyAPIView):
    queryset = ServiceDealer.objects.all()
    serializer_class = serializers.ServiceDealerAllSerializer
    lookup_field = "id"
