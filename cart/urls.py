from django.conf.urls import url, include
from . import views

urlpatterns =[
		url(r'^$', views.viewCart, name = 'mycart'),
		url(r'^(?P<id>\d+)$', views.update_cart, name = 'update_cart' ),
]