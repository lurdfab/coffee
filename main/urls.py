from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('products', views.products, name='products'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
]
