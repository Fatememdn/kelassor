from django.db import models
from accounts.models import Seller, Customer

class user_order(models.Model):
    user = models.OneToOneField(Customer)
    # product = models.
