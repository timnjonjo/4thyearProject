from django.db import models
from products.models import *
# Create your models here.

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank = True)
	product = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)
	price = models.DecimalField(max_digits=100, decimal_places =2, default =0.00)

	def __str__(self):
		return str(self.cart.id)

class Cart(models.Model):
	total= models.DecimalField(max_digits=100, decimal_places= 2, default=0)
	timestamp = models.DateTimeField(auto_now_add= True, auto_now=False)
	updated = models.DateTimeField(auto_now_add= False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return "Cart Id: %s" %(self.id)