from typing import ContextManager
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_cutomers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders' : orders, 
               'customers' : customers,
               'total_orders' : total_orders,
               'delivered' : delivered,
               'pending' : pending
               }

    return render(request, 'accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products' : products})

def customer(request, pk_test):
    customer = Customer.objects.get(id = pk_test)
    
    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {'customer' : customer, 'orders' : orders, 'orders_count':orders_count}
    return render(request, 'accounts/customer.html', context)

def all_customers(request):
    all_customers_data = Customer.objects.all()
    
    #orders = customer.order_set.all()
    #orders_count = orders.count()
    #context = {'customer' : all_customer_data, 'orders' : orders, 'orders_count':orders_count}

    #context = {'customer' : all_customers_data}
    #return render(request, 'accounts/all_customers.html', context)
    #products = Product.objects.all()
    return render(request, 'accounts/all_customers.html', { 'all_customers_data': all_customers_data})

def all_orders(request):
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders' : orders, 
               'total_orders' : total_orders,
               'delivered' : delivered,
               'pending' : pending
               }

    products = Product.objects.all()
    return render(request, 'accounts/all_orders.html', context)

def createOrder(request):

    form = OrderForm()

    if request.method == 'POST' :
        #print('Printing POST: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form }

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}

    if request.method == 'POST' :
        #print('Printing POST: ', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item' : order}
    return render(request, 'accounts/delete.html', context)


def createProduct(request):

    form = ProductForm()

    if request.method == 'POST' :
        #print('Printing POST: ', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form }

    return render(request, 'accounts/product_form.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    context = {'form': form}

    if request.method == 'POST' :
        #print('Printing POST: ', request.POST)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/')
    context = {'item' : product}
    return render(request, 'accounts/delete_product.html', context)

def createCustomer(request):

    form = CustomerForm()

    if request.method == 'POST' :
        #print('Printing POST: ', request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form }

    return render(request, 'accounts/customer_form.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    context = {'form': form}

    if request.method == 'POST' :
        #print('Printing POST: ', request.POST)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/customer_form.html', context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('/')
    context = {'item' : customer}
    return render(request, 'accounts/delete_customer.html', context)