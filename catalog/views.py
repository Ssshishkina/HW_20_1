from django.shortcuts import render, get_object_or_404

from catalog.models import Product

def home(request):
    '''Выводит на страницу все товары'''
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/product_list.html', context)


def product_info(request, pk):
    '''Выводит на страницу товар по pk.'''
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/product_info.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    context = {
        'title': 'contact'
    }
    return render(request, 'catalog/contacts.html', context)

