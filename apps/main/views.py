from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.
from rest_framework.parsers import FormParser , MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response




class SlugRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"




class AnnouncementView(generics.CreateAPIView):
    serializer_class = AnnouncementAllSerializer
    parser_classes = (FormParser , MultiPartParser)
    queryset = Announcement.objects.all()





class PriceView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Prices.objects.first()
        serializer = PricesSerializer(queryset, context={"request": request})
        return Response(serializer.data)


class PricesUpdateView(generics.UpdateAPIView):  
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer
    lookup_field = "id"





class PriceALLView(generics.ListAPIView):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer

    def get_queryset(self):
        return self.queryset.filter()



class PiricesView(generics.CreateAPIView):
    serializer_class = PricesSerializer
    queryset = Prices.objects.all()




    
    




class CarOptionView(generics.CreateAPIView):
    serializer_class = CarOptionSerializer
    queryset = CarOption.objects.all()


class CarOptionMappingView(generics.ListAPIView):
    queryset = CarOptionsMapping.objects.all()
    serializer_class = CarOptionsMappingSerializer

    def get_queryset(self):
        return self.queryset.filter()


    
class BodyPartView(generics.CreateAPIView):
    serializer_class = BodyPartsSerializer
    queryset = BodyParts.objects.all()


class BodyConditionsView(generics.CreateAPIView):
    serializer_class = BodyConditionsSerializer
    queryset = BodyConditions.objects.all()


    def get_queryset(self):
        return self.queryset.filter()
    

class BodyStatusView(generics.ListAPIView):
    serializer_class = BodyStatusSerializer
    queryset = BodyStatus.objects.all()
    


class ImagesView(generics.CreateAPIView):
    parser_classes = (FormParser , MultiPartParser)
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()





class AnnouncementDetailView(SlugRetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSingleSerializer




    