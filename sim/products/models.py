from django.db import models
from accounts.models import Seller, Customer

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True) 
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ManyToManyField(Customer)
    price = models.IntegerChoices()
    