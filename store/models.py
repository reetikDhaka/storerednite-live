from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

class Customer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=False,null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    def __str__(self):
       return self.name

class Product(models.Model):
    name= models.CharField(max_length=120, blank=False,null=True)
    image = models.ImageField(null=True,blank=True)
    price = models.FloatField()
    slug = models.SlugField(blank=True,unique=True)
    digital = models.BooleanField(default=False, null=True,blank=False)
    categories = models.CharField(default='Unknown',null=True, blank=False,max_length=120)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    compelete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(blank=True,null=False,max_length=10)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.product.price *self.quantity
        return total

#for testing only
class testModel(models.Model):
    username= models.CharField(max_length=120)
    likes = models.IntegerField()
    def __str__(self):
        return str(self.likes)


def slug_generator(sender, instance, *args,**kwargs):
    if not instance.slug:

        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator,sender=Product)

#login model
class UserLogin(models.Model):
    username = models.CharField(max_length=12, null=True,blank=False);
    password = models.CharField(max_length=120, blank=False,null=True);
    def __str__(self):
        return self.username

class UserRegistration(models.Model):
    username = models.ForeignKey
