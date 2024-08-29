from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    is_Confirmed = models.BooleanField(default= False)
     
    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    wallet = models.IntegerField(default=100)

    def __str__(self):
        return self.name