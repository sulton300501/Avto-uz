from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics

class ComparisonsView(generics.ListAPIView):
    queryset = Comparisons.objects.all()
    serializer_class = ComparisonSerializer

    def get_queryset(self):
        return self.queryset.filter()


class CreateComporisonView(generics.CreateAPIView):
    queryset = Comparisons.objects.all()
    serializer_class = ComparisonSerializer
    



class FavouritesView(generics.ListAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavouritesSerializer

    def get_queryset(self):
        return self.queryset.filter()
    

class InspectionPlaceView(generics.CreateAPIView):
    queryset = InspectionPlace.objects.all()
    serializer_class = InspectionPlaceSerializer
    