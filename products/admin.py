from django.contrib import admin
from .models import Product, Product_image, Store, Product_price, Category, Subcategory


class PriceAdmin(admin.StackedInline):
	model = Product_price

class MymodelAdmin (admin.ModelAdmin):
	list_display = ['title','availability','category', 'dateadded', 'lastmodified']
	inlines = [ PriceAdmin]


class StoreAdmin(admin.ModelAdmin):
	list_display =['store_name', 'location', 'email','lastupdated']
	class meta:
		model = Store

class pricesAdmin(admin.ModelAdmin):
	list_display =['product', 'store', 'price']
	class meta:
		model = Product_price

admin.site.register(Subcategory)
admin.site.register(Product, MymodelAdmin)
admin.site.register(Product_image)
admin.site.register(Store, StoreAdmin)
admin.site.register(Product_price, pricesAdmin)
admin.site.register(Category)