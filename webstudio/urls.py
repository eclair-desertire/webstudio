from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.main_page,name='main_page'),
    path('order_new/',views.order_new,name='order_new'),
]