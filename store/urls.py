"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import home,product_detail,index_db,detail,delete,search

urlpatterns = [
    
    path('home/',home, name='home'),
    path('products/<int:id>/',product_detail , name='product_detail'),
    path('db/',index_db, name='index_db'),
    path('detail/<int:id>', detail, name='detail'),
    path('db/<int:id>/delete',delete, name='delete'),
     path('search/', search, name='search'),
   
]



