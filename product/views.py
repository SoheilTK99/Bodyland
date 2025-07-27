from django.shortcuts import render , get_object_or_404
from .models import Product 

def product_type(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render (request,"product/product.html",context)





def product_list(request, category):
    products = Product.objects.filter(product_categorey=category)
    return render(request, 'product/product_list.html', {
        'products': products,
        'category': category
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {
        'product': product
    })