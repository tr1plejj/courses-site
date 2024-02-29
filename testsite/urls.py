from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('add_product/<int:pk>', views.add_product, name='add_product'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('register', views.register, name='register')
]
