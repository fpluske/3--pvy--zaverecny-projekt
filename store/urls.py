from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produkty/', views.product_list, name='product_list'),
    path('produkty/<slug:slug>/', views.product_detail, name='product_detail'),
]