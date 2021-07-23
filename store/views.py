from django import forms
from django.contrib.admin.decorators import action
from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import json
import logging
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control
from .models import *
from .forms import *
from django.contrib import messages
logging.basicConfig(filename='user-data.log', level=logging.INFO,format= '%(asctime)s %(message)s')
@login_required(login_url='login-page')
def home_view(request):
    try:
        customer = request.user.customer
        obj = Order.objects.get(customer=customer)
    except:
        obj=[]
    if request.user is not None:
        print(request.user)
        user = User.objects.get(username = request.user)
        if Customer.objects.filter(user=request.user).exists():
            print(request.user)
            print(Customer.objects.filter(user=request.user).exists())
        else:
            print('createing customer')
            Customer.objects.create(user=user, name=user.username)
    obj1 = Product.objects.all()
    print(obj1.__len__());
    return render(request, 'home.html', {'products': obj1, 'obj':obj})
def other_pages(request):
    obj1 = Product.objects.all()[8:]
    return render(request, 'secondpage.html', {'products': obj1})


def checkout_view(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order,created = Order.objects.get_or_create(customer=customer)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total':0,
                    'get_cart_item': 0}
    except:
        items=[]
        order = []
    context={
            'items':items,
             'order': order



        }
    return render(request, 'ordersummary.html', context)

@cache_control(max_age=3600)
def cart_view(request):
    
    try:
        customer = request.user.customer
        obj = Order.objects.get(customer=customer)
    except:
        obj=[] 
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order,created = Order.objects.get_or_create(customer=customer)
            items = order.orderitem_set.all()
        else:
            cart = json.loads(request.COOKIES['cart'])
            print(cart)
            items = []
            order = {'get_cart_total':0,
                    'get_cart_item': 0}
    except:
        items = []
        order =[]
    context={
            'items':items,
             'order': order,
             'obj': obj


        }
    return render(request,'cartpage.html', context)

def updatecart_view(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']
     print(productId)
     product = Product.objects.get(id=productId)
     customer = request.user.customer
     order , created = Order.objects.get_or_create(customer=customer)
     orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
     if action == 'add':
         orderItem.quantity = (orderItem.quantity +1)
         logging.info(f'user:{customer} added item in cart productId:{productId}')
         orderItem.save()
     elif action == 'remove':
         orderItem.quantity = (orderItem.quantity -1)

         orderItem.save()
     elif action == 'delete':
         logging.info(f'user:{customer} removed item in cart productId:{productId}')
         orderItem.delete()

     if orderItem.quantity<=0:
         orderItem.delete()
         logging.info(f'user:{customer} removed item in cart productId:{productId}')

     return JsonResponse('item is added to the cart', safe=False)


def product_display_view(request,slug):
    obj = Product.objects.get(slug=slug)
    return render(request, 'displayproduct.html',{'object': obj})



def base_view(request):
    customer = request.user.customer
    obj=Order.objects.get(customer=customer)
    return render(request,'base.html',{'obj':obj})


def login_view(request):
    var=False
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('logged in')
            login(request,user)
            return redirect('home-page')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'loginpage.html')


def logout_view(request):
    logout(request)
    return redirect('login-page')
    
def registration_view(request):
    form = CreateUserForm()
    try:
        if request.method== 'POST':
            form = CreateUserForm(request.POST)
            if request.POST['password1']!= request.POST['password2']:
                messages.error(request, "your passwords don't match,try again!")
            if form.is_valid:
                form.save()
                return redirect('login-page')
    except:
        pass
        messages.error(request,'check your password(it should consist of 8 letters)')
                
    
    context = {
     'form': form
    }
    return render(request, 'registration.html',context)

def customer_display_view(request):
    obj = Customer.objects.all()
    return render(request,'customer-display.html',{'obj':obj})

# for testing

def test_view(request):
    
    return render(request,'test.html')


def test_api(request):
    data = json.loads(request.body)
    username = data['username']
    action = data['action']
    testobj , created = testModel.objects.get_or_create(username=username, likes = 1)
 
    return JsonResponse('', safe=False)