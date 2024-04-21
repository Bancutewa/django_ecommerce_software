from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .models import *
import json
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    products = Product.objects.all()
    context = {'products' : products,'items':items, 'order':order, 'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/index.html",context)
def ProductList(request):
    products = Product.objects.all()
    customer = request.user
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    items = order.orderitem_set.all()
    context = {'products' : products,'items':items, 'order':order}
    return render(request,"myapp/product.html",context)
def ProductDetails(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    id = request.GET.get('id', '')
    products = Product.objects.filter(id = id)
    context = {'products' : products, 'items':items, 'order':order,'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/productdetails.html", context)
def Cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_login = "show"
        user_not_login = "hidden"
        
    else:
        items= []
        order = {"get_cart_items":0,"get_cart_total":0 }
        cartItems = order['get_cart_items']
        user_login = "hidden"
        user_not_login = "show"
        
    context = {'items':items, 'order':order, 'user_login':user_login, 'user_not_login':user_not_login }
    return render(request,"myapp/cart.html",context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    elif action == 'delete':
        orderItem.delete()
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("added",safe=False)

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
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        user_login = "show"
        user_not_login = "hidden"
    else:
        user_login = "hidden"
        user_not_login = "show"
    context = {'user_login':user_login,'items':items, 'order':order, 'user_not_login':user_not_login }

    return render(request,"myapp/contact.html",context)