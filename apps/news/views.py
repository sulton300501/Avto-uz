from django.shortcuts import render
from rest_framework import generics
from .serializers import ReelSerializer
from .models import *
from rest_framework.parsers import FormParser , MultiPartParser
from rest_framework.views import APIView





class CreateReelsAPIView(generics.CreateAPIView):
    parser_classes = (FormParser,MultiPartParser)
    serializer_class = ReelSerializer
    queryset = Reels.objects.all()



class ReelAPIView(generics.ListAPIView):
    queryset = Reels.objects.all()
    serializer_class = ReelSerializer

    def get_queryset(self):
        return self.queryset.filter()

    






