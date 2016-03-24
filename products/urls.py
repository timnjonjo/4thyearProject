from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns =[

	url(r'^$', views.all_products, name = 'Products' ),
	url(r'^(?P<id>\d+)$', views.product_detail, name = 'Product_Detail' ),

]