from django.urls import path

from django.urls import url

from .import views

urlpattrens = [ 
    path('',views.index,name='index'),
    url('', views.index, name='index'),
]
