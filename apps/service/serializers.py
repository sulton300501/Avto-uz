from rest_framework import serializers
from .models import *




class ServiceDealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDealer
        fields = (
            "type",
            "dealer_sub_type",
            "name",
            "address",
            "phone_number",
            "working_hours",
            "number_of_cars",
            "logo",
            "location_url",
            # "latitude",
            # "longitude",
            "description"
            )


class ServiceDealerAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDealer
        fields = (
             "type",
            "dealer_sub_type",
            "name",
            "address",
            "phone_number",
            "working_hours",
            "number_of_cars",
            "logo",
            "latitude",
            "longitude",
            "description"
        )