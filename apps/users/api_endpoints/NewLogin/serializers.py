from rest_framework import serializers 
from django.core.cache import cache
from django.core.exceptions import ValidationError
import random
from django.contrib.auth import get_user_model


User = get_user_model()



class NewLoginSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r"^\+998\d{9}$",
        error_messages = {
            "Invalid":"Phone number must be in the format +9989xxxxxxxx."
        }
    )



    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        otp_first_code = random.randint(100000 , 999999)
        print(otp_first_code)
        otp_first_key = f"otp_{phone_number}"


        otp_get_key = cache.get(otp_first_key)

        if otp_get_key:
            raise ValidationError({
                "error":"already send code",
                "message":"We have alreat sent"
            })
        

        User.objects.get_or_create(phone_number=phone_number , username=phone_number)

        cache.set(otp_first_key  , otp_first_code , 60 )

        return {"message":"OTP key sent successfully"}
    
        
        


        



        
    






