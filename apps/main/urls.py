from django.urls import path
from apps.main import views


urlpatterns = [
    path('main/create/Announcement/', views.AnnouncementView.as_view(),name="announcement"),
    path('main/getLast/price/', views.PriceView.as_view() , name="price"),
    path("main/getAll/price/", views.PriceALLView.as_view(), name="all-price"),
    path('main/add/price/',views.PiricesView.as_view(),name="add-price"),
    path('main/add/carOption/', views.CarOptionView.as_view() , name="car-option"),
    path('main/getAll/carOptionMapping/', views.CarOptionMappingView.as_view(), name="car-option-mapping"),
    path('main/add/bodyPart/',views.BodyPartView.as_view(),name="bodyPart"),
    path('main/getAll/BodyCondition/', views.BodyConditionsView.as_view(),name="body-condition"),
    path('main/add/Images/',views.ImagesView.as_view(),name="images"),
    path('main/getDetail/Announcement/<slug:slug>/', views.AnnouncementDetailView.as_view() , name="announcement-detail"),
    path('main/prices/<int:id>/', views.PricesUpdateView.as_view(), name="price-update"),

]

