from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def all_products(request):
	products= Product.objects.all()
	template = 'sample.html'
	context = {"products":products}
	return render ( request, template, context)


def product_detail(request, id):
	product= Product.objects.get(id=id)
	template = 'product_detail.html'
	context = {"product":product}
	return render ( request, template, context) 