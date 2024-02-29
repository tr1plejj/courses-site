from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products, name='get_products'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('add_product/<int:pk>', views.add_product, name='add_product'),
    path('user', views.user_profile, name='user_profile'),
]
