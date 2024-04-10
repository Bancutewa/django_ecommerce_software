
from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path("",views.Home, name="home"),
    path("product/", views.ProductList, name="product"),
    path("details/", views.ProductDetails, name="details"),
    path("cart/", views.Cart, name="cart"),
    path("register/", views.Register, name="register"),
    path("login/", views.LoginPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
    path("contact/", views.Contact, name="contact"),
]
