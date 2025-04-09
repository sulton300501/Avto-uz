from django.urls import path
from apps.service import views

urlpatterns = [
    path("service/add/ServiceDealer/", views.ServiceDealerView.as_view(), name="service-dealer"),
    path("service/getAll/ServiceDealler/",views.ServiceDealerAllView.as_view() , name="serviceDealer-all"),
     path("service/delete/ServiceDealler/<int:id>/",views.ServiceDealerDeleteView.as_view() , name="serviceDealer-delete"),
 
]
