from django.db import models
from django.db.models import ImageField

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    direction = models.CharField(max_length=200, blank=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}'

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(blank=False)
    sum = models.IntegerField(blank=False, null=True)
    date = models.DateField(auto_now=True)
    image = ImageField(upload_to='shopapp/images/', default=None, null=True, blank=True)

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Username: {self.customer}, date_ordered: {self.date_ordered }'