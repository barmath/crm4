from django import forms
from django.forms import ModelForm, fields, widgets
from django.shortcuts import render
from .models import Order, Product, Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
       


