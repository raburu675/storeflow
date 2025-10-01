from django.db import models


# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)    
    price = models.DecimalField(default=0 ,decimal_places=2, max_digits=10)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)    
    # image = models.ImageField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 , decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#customer orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    # date = models.DateField(default=datetime.datetime.today)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.product)