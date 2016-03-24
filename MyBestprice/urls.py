"""MyBestprice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^products/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
	url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    



    #user authentication urls
    url(r'^accounts/register/', views.register_user, name='register'),
    url(r'^accounts/login/', views.login, name='login'),
    url(r'^accounts/auth', views.auth_view),
    url(r'^accounts/logout', views.logout),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)