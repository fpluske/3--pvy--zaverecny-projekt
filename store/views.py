from django.shortcuts import get_object_or_404, render

from .models import Product, Category


def home(request):
    featured_products = Product.objects.select_related('category', 'manufacturer').filter(featured=True)[:3]
    latest_products = Product.objects.select_related('category', 'manufacturer').order_by('-id')[:6]
    return render(
        request,
        'store/home.html',
        {
            'featured_products': featured_products,
            'latest_products': latest_products,
        },
    )


def product_list(request):
    products = Product.objects.select_related('category', 'manufacturer').all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product.objects.select_related('category', 'manufacturer'), slug=slug)
    related_products = (
        Product.objects.select_related('category', 'manufacturer')
        .filter(category=product.category)
        .exclude(pk=product.pk)[:3]
    )
    return render(
        request,
        'store/product_detail.html',
        {
            'product': product,
            'related_products': related_products,
        },
    )


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.select_related('manufacturer').filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})

