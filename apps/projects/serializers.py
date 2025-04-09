from rest_framework import serializers
from .models import *




class ComparisonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comparisons
        fields = ("id","car_id","user_id")




class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"


class InspectionPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionPlace
        fields = ("id","region","district")