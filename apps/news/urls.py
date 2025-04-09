from django.urls import path
from apps.news import views



urlpatterns = [
    path('news/add/reels/' , views.CreateReelsAPIView.as_view() , name="add-reels"),
    path('news/GetAll/reels/' , views.ReelAPIView.as_view(),name="getall-reels"),
]
