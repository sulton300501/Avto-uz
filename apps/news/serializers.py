from  rest_framework import serializers
from .models import *



class ReelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reels
        fields = [ 
          "user",
          "announcement",
          "entities_id",
          "video_url",
          "caption",
          "likes",
          "view_count",
           
            ]
        


