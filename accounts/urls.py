from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('products/', views.products, name="products"),
    path('all_customers/', views.all_customers, name="all_customers"),
    path('all_orders/', views.all_orders, name="all_orders"),
    path('customer/<str:pk_test>', views.customer, name="customer"),
    
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),

    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>', views.deleteProduct, name="delete_product"),

    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>', views.deleteCustomer, name="delete_customer")
]