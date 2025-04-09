from  rest_framework import serializers
from .models import *
from apps.common.serializers import ThumbnailImageSerializer







class AnnouncementAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = [ 

            "user_id",
            "dealer_id",
            "brand",
            "model",
            "year",
            "price",
            "milage",
            "color",
            "engine_capacity",
            "gearbox_type",
            "fuel_type",
            "gas_type",
            "description",
            "generation",
            "body_type",
            "power",
            "passport_type",
            "purchase_date",
            "ownership_type",
            "status",
            "favorite_count",
            "slug",
            "inspection_place",
           
            ]
        





class PricesSerializer(serializers.ModelSerializer):
    # announcement = AnnouncementSerializer()
    class Meta:
        model = Prices
        fields = [
          "id",
          "car_id",
           "price",
           "currency",
           "discount",
            ]

        



class CarOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOption
        fields = [ 
            
           "name",
            ]




class CarOptionsMappingSerializer(serializers.ModelSerializer):
    # announcement = AnnouncementAllSerializer()
    # caroption = CarOptionSerializer()
    class Meta:
        model = CarOptionsMapping
        fields = [ 
           "car_id",
           "car_options_id"
            ]
    






class BodyPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyParts
        fields = [ 
           "body_name"
            ]
        


class BodyConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyConditions
        fields = [ 
           "condition_name"
            ]
        


class BodyStatusSerializer(serializers.ModelSerializer):
    announcemet = AnnouncementAllSerializer()
    body_part = BodyPartsSerializer()
    condition = BodyConditionsSerializer()
    class Meta:
        model = BodyConditions
        fields = [ 
           "announcemet"
           "body_part",
           "condition"
            ]
        



class ImagesSerializer(serializers.ModelSerializer):
    thumbnail_image_url = ThumbnailImageSerializer(source="image_url", read_only=True)
    # announcement = AnnouncementSerializer()
    image_url = serializers.ImageField(write_only=True)
    class Meta:
        model = Images
        fields = [
            "car_id",
           "thumbnail_image_url",
           "image_url",
           "is_main",
            ]






class AnnouncementSingleSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = Announcement
        fields = (
            "image",
            "brand",
            "year",
            "price",
            "milage",
            "description",
            "slug",

        )


    def get_image(self , obj):
        get_image_option = Images.objects.filter(car_id=obj.id)
        get_image = ImagesSerializer(get_image_option , many=True).data
        return get_image
