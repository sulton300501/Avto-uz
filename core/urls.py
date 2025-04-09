from django.contrib import admin
from django.urls import path , include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

from .schema import swagger_urlpatterns



urlpatterns = [
    path("i18n/", include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(path('admin/',admin.site.urls))

urlpatterns += swagger_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/' , include('apps.common.urls')),
    path('api/v1/' , include('apps.main.urls')),
    path('api/v1/', include('apps.news.urls')),
    path('api/v1/', include('apps.projects.urls')),
    path('api/v1/', include('apps.service.urls')),
]



