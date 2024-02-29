from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def get_products(request):
    products = Product.objects.all()
    return render(request, 'testsite/products.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'testsite/product_detail.html', {'product': product})


def add_product(request, pk):
    # pk - id продукта
    # id = authorized user и передавать его в redirect
    return redirect('user_profile')


def user_profile(request, pk):
    pass

