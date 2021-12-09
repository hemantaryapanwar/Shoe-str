from django.contrib import admin
from django.urls import path 
from Home import views
urlpatterns = [
    
   path("",views.index,name='Home'),
   path("about",views.about,name='about'),
   path("contact",views.contact,name='contact'),
   path("shoes",views.shoes,name='shoes'),
   path("index",views.index,name='ho') ,
   path("product",views.product,name='product'),
   path("sports",views.sports,name='sports') ,
   path("sneaker",views.sneakers,name='sneaker'),
   path("checkout",views.checkout,name='checkout')  


]
