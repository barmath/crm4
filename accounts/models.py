from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    data_de_nascimento = models.DateTimeField(max_length=200, null=True)
    cpf = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = ( 
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door'),
    )

    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY) # SUBSTITUIR PARA CODIGO DA CATEGORIA
    quantidade_em_estoque = models.FloatField(null=True)
    preco_de_compra = models.FloatField(null=True)
    price = models.FloatField(null=True) # SUBSTITUIR PARA PRECO DE VENDA
    margem = models.FloatField(null=True) 
    detalhes = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = ( 
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for delivery'),
        ('Delivered','Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) #EXPLICAR OU ALTERAR ISSO
    #product = ManyToManyField(Product)
    preco_do_produto = models.FloatField(null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.product.name
