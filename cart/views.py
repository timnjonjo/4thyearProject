from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Cart, CartItem
from products.models import Product, Store, Product_price
# Create your views here.
@login_required
def viewCart(request):
	stores = Store.objects.all()
	selected_store = request.GET.get('selected_store')
	if not selected_store:
		selected_store =1
	thestore = Store.objects.get(id=selected_store)
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		if selected_store:
			for item in cart.cartitem_set.all():
				try:
					tprice = Product_price.objects.get(product =item.product, store_id=selected_store)
				except:
					tprice= None
				if tprice:
					the_price = tprice.price
					item.price = the_price
					item.save()
				else:
					the_price=0.00
					item.price = the_price
					item.save() 
		new_total = 0.00
		for item in cart.cartitem_set.all():
			price = float(item.price)
			new_total+=price
			cart.total =new_total
			cart.save()
		context = {"cart":cart, "stores":stores , "thestore":thestore}
	else:
		empty_message ="Your Cart is Empty. Please Continue Shopping."
		context ={"Empty": True , "empty_message": empty_message}

	template = 'viewcart.html'
	return render(request, template, context)

# def viewCart(request):
# 	stores = Store.objects.all()
# 	cart = Cart.objects.all()[0]
# 	product = Product.objects.all()

# 	selected_store = request.GET.get('selected_store')
# 	if selected_store:
# 		for items in cart.products.all():
# 			price = items.product_price_set.filter(store_id=selected_store)
# 		context = {"cart":cart, "stores":stores, "price": price}
# 		template = 'viewcart.html'
# 	else:
# 		for item in cart.products.all():
# 			prices = Product_price.objects.filter(store_id=1, product_id=item.products)
# 		context = {"cart":cart, "stores":stores, "prices":prices}
# 		template = 'viewcart.html'
# 	return render(request, template, context)

def update_cart (request , id):
	request.session.set_expiry(120000)
	try:
		the_id= request.session['cart_id']
	except:
		new_cart= Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id= new_cart.id
	cart = Cart.objects.get(id= the_id)
	try:
		product = Product.objects.get(id=id)
	except Product.DoesNotExist:
		pass

	cart_item, created =CartItem.objects.get_or_create(cart =cart, product=product)
	if created:
		print ("RAAAAAH")

	tprice = Product_price.objects.get(product =product, store_id=1)
	the_price = tprice.price
	cart_item.price = the_price
	cart_item.save()
	# if not cart_item in cart.items.all():
	# 	cart.items.add(cart_item)
	# else:
	# 	cart.items.remove(cart_item)

	return HttpResponseRedirect (reverse("mycart"))
