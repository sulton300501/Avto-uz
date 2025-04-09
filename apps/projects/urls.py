from django.urls import path
from apps.projects import views

urlpatterns = [
    path("project/GetAllComporison/", views.ComparisonsView.as_view(), name="comporison"),
    path("project/add/comporison/",views.CreateComporisonView.as_view(),name="add-comporison"),
    path("project/GetallFavourites/",views.FavouritesView.as_view() , name="favourites"),
    path("project/add/InspectionPlace/",views.InspectionPlaceView.as_view() , name="inspection"),
]
