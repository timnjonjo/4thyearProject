from django.db import models
from django.utils import timezone


#model product

class Category(models.Model):
	category_name = models.CharField(max_length = 50)
	category_description = models.TextField()
	timestamp = models.DateTimeField( auto_now_add = True, auto_now =False)

	def __str__(self):
		return self.category_name


class Subcategory(models.Model):
	category = models.ForeignKey(Category)
	title =models.CharField(max_length=60)
	description = models.TextField()

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length = 50, unique= True)
	description = models.TextField()
	availability = models.BooleanField(default = True)
	category = models.ForeignKey(Subcategory)
	dateadded = models.DateField(auto_now_add= True, auto_now= False)
	lastmodified = models.DateTimeField(auto_now_add = False , auto_now= True)
	#price = models.ForeignKey('Product_price')

	def __str__(self):
		return self.title




class Store(models.Model):
	store_name = models.CharField(max_length =100, blank= False, null= False)
	location = models.CharField(max_length= 100, blank =True, null =True)
	store_description = models.TextField()
	email = models.EmailField()
	Added = models.DateTimeField(auto_now=False, auto_now_add =True)
	lastupdated = models.DateTimeField(auto_now =True, auto_now_add = False)

	def __str__(self):
		return self.store_name

class Product_price(models.Model):
	store= models.ForeignKey(Store)
	product = models.ForeignKey(Product)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	updated_at =  models.DateTimeField(auto_now_add= False, auto_now = True)

	def __str__(self):
		return self.product.title



class Product_image(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to= 'products/images/' ,null=True, blank=True)

	def __str__(self):
		return self.product.title