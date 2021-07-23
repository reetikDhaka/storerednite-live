from os import name
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('', home_view, name = 'home-page'),
    path('checkout', checkout_view, name='checkout-page'),
    path('cart', cart_view,name='cart-page'),
    path('update-cart',updatecart_view,name='update-cart'),
    path('product/<slug:slug>', product_display_view ,name='single-product-page'),
    path('mytest', test_view),
    path('test/base',base_view),
    path('login', login_view, name= 'login-page'),
    path('logout', logout_view,name='logout'),
    path('registration', registration_view,name='registration-page'),
    path('customers', customer_display_view,name='customer-count-page'),
    path('page2', other_pages, name='second-page'),
     path('mytest/jsonrequest',test_api ),
]
urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
