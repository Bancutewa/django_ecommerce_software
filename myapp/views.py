from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"myapp/index.html")
def Product(request):
    return render(request,"myapp/product.html")
def ProductDetails(request):
    return render(request,"myapp/product-details.html")
def Cart(request):
    return render(request,"myapp/cart.html")
def Register(request):
    return render(request,"myapp/cart.html")
def LoginPage(request):
    return render(request,"myapp/cart.html")
def Contact(request):
    return render(request,"myapp/contact.html")