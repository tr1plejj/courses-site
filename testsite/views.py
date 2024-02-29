from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegisterForm
from .models import Product, Profile


def all_products(request):
    products = Product.objects.all()
    return render(request, 'testsite/products.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'testsite/product_detail.html', {'product': product})


@login_required
def add_product(request, pk):
    # pk - id продукта
    user = Profile.objects.get(user=request.user.pk)
    product = Product.objects.get(pk=pk)
    user.purchased_products.add(product)
    return redirect('user_profile', )


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user.pk)
    products = profile.purchased_products.all
    return render(request, 'testsite/user_profile.html', {'products': products})


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('user_profile')
        else:
            return render(request, 'registration/register.html', {'form': form})
