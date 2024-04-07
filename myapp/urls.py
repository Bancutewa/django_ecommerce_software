
from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path("",views.Home, name="home"),
    path("product/", views.Product, name="product"),
    path("details/", views.ProductDetails, name="product_details"),
    path("cart/", views.Cart, name="cart"),
    path("register/", views.Register, name="register"),
    path("login/", views.LoginPage, name="login"),
    path("contact/", views.Contact, name="contact"),
]
