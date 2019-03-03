from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from .models import Type, Product

def index(request):
    type_objs = Type.objects.filter(active__exact=True)
    context = {
        'type_objs': type_objs,
    }
    return render(request, "ecommerce/type.html", context)

def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    
    return render(request, 'ecommerce/product.html', {'product': product})
