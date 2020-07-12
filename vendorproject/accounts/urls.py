from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products', views.products,name='products'),
    path('customer/<str:keyy>/', views.customer,name='customer'),
    path('create_order/<str:keyy>', views.create_order, name='create_order'),
    path('create_order/', views.create_order, name='create_order'),
    path('add_product', views.add_product,name='add_product'),
    path('update_order/<str:pk>',views.update_order,name='update_order'),
    path('delete_order/<str:pk>',views.delete_order,name='delete_order'),
    ]
