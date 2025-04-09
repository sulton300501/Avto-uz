from django.urls import path
from apps.common import views



urlpatterns = [
    path("common/GetAllSetting/", views.SiteSettingView.as_view() ,name="setting"),
]
