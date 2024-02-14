from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('getproducts', views.getProducts, name="getproducts"),
    path('getproducts/<str:pk>', views.getProduct, name="getproduct"),  # WORKING
]
