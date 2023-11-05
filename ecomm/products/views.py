from django.shortcuts import render
from products.models import Product



def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)

        if request.GET.get('size'):
            size = request.GET.get('size')
            print(size)

        return render(request, 'product/product.html', context = {'product' : product})

    except Exception as e:
        print(e)