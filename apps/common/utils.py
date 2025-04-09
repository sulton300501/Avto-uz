import os
from django.utils import dateformat , timezone




def generate_upload_path(instance , filename):
    app_label = instance._meta.app_label
    model_name = instance._meta.model_name
    now = dateformat.format(timezone.now() , 'Y-m-d H:i:s')
    file , exc = split_file_name(filename)

    filepath = "%s%s%s-%s.%s" % (
        app_label , model_name , file ,now , exc
    )

    return filepath




def split_file_name(filename):
    return [''.join(filename.split('.')[:-1]) , filename.split('.')[-1]]



