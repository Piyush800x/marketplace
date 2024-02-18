from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.getProducts, name="getproducts"),
    path('products/<str:pk>', views.getProduct, name="getproduct"),  # WORKING
]
