from django.contrib import admin
from .models import Categorie, Customer, Product, Order

admin.site.register(Product)
admin.site.register(Categorie)
admin.site.register(Customer)
admin.site.register(Order)
