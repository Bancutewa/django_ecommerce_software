from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .models import *
import json
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        customer = request.user
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    products = Product.objects.all()
    context = {'products' : products, 'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/index.html",context)
def ProductList(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request,"myapp/product.html",context)
def ProductDetails(request):
    if request.user.is_authenticated:
        customer = request.user
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    id = request.GET.get('id', '')
    products = Product.objects.filter(id = id)
    context = {'products' : products, 'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/productdetails.html", context)
def Cart(request):
    if request.user.is_authenticated:
        customer = request.user
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    context = {'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/cart.html",context)
def Register(request):
    if request.user.is_authenticated:
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form':form, 'user_login':user_login, 'user_not_login':user_not_login}
    return render(request,"myapp/register.html", context)
def LoginPage(request):
    if request.user.is_authenticated:
        user_login = "show"
        user_not_login = "hidden"
        return redirect('home')
    else:
        user_login = "hidden"
        user_not_login = "show"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        user_by_username = User.objects.filter(username=username).first()
        if user is not None:
            login(request, user)
            return redirect('home')
        elif user_by_username is None: messages.info(request, 'Username chưa được đăng kí')
        else: messages.info(request, 'Nhập sai mật khâu')
    context = { 'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/login.html", context)
def LogoutPage(request):
    logout(request)
    return redirect('home')
def Contact(request):
    if request.user.is_authenticated:
        customer = request.user
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    context = {'user_login':user_login, 'user_not_login':user_not_login }

    return render(request,"myapp/contact.html",context)