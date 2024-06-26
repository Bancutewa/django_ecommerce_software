from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(null=True,max_length=2000)
    description = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    date_order = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    
    def __str__(self):
        return str(self.id)
    # Ham tra ve total items in Order 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
        # Ham tra ve total price in Order 
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank= True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True   )
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
