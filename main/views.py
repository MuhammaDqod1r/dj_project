from multiprocessing import context
from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import qrcode
from django.contrib import messages
# Create your views here.




def index(request):
    product_discount = Product_discount.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()[:8]
    products = Product.objects.all().order_by('-id')[:8]
    s_image = Slider_image.objects.all()[:6]
    logo = Site_logo.objects.last()
    our_brands = Our_brands.objects.all()[:6]
    
    
    context = {
        'product_discount': product_discount,
        'categories': categories,
        'products': products,
        's_image': s_image,
        "logo": logo,
        'our_brands': our_brands,
    }
    return render(request, 'index.html', context)



def product_single(request, pk):
    categories = Category.objects.all()[:8]
    product = Product.objects.get(id=pk)
    logo = Site_logo.objects.last()
    
    

    context = {
        'product': product,
        'categories': categories,
        "logo": logo,
    }

    return render(request, 'products-single.html', context)


def product_single_discount(request, pk):
    categories = Category.objects.all()[:8]
    product = Product_discount.objects.get(id=pk)
    logo = Site_logo.objects.last()
    


    context = {
        'product': product,
        'categories': categories,
        'logo': logo,
    }

    return render(request, 'products-single.html', context)


def add_product(request):
    categories = Category.objects.all()
    context = {
        'cats': categories,
    }
    return render(request, 'add_product.html', context)


def adds_product(request):
    if request.method == 'POST':
        name = request.POST.get('pr_name')
        characters = request.POST.get('pr_characters')
        cat_id = request.POST.get('pr-category')
        image = request.FILES['pr_image']
        quantity = request.POST.get('pr_quantity')
        price = request.POST.get('pr_price')
        category = get_object_or_404(Category, id=cat_id)
        product = Product.objects.create(name=name, characters=characters, category=category,
                                         image=image, quantity=quantity, price=price)
        
        pr_qrcode = qrcode.make(f'http://192.168.43.46/product_single/{product.id}/')
        pr_qrcode.save(f'media/pr_qrcodes/{product.id}.jpg')
        
        return redirect('add_product')
    
    


def add_discount__product(request):
    categories = Category.objects.all()
    context = {
        'cats': categories,
    }
    return render(request, 'add-discount__product.html', context)



def adds_discount__product(request):
    if request.method == 'POST':
        name = request.POST.get('pr_name')
        characters = request.POST.get('pr_characters')
        cat_id = request.POST.get('pr-category')
        image = request.FILES['pr_image']
        quantity = request.POST.get('pr_quantity')
        price = request.POST.get('pr_price')
        discount = request.POST.get('pr_discount')
        category = get_object_or_404(Category, id=cat_id)
        product = Product_discount.objects.create(name=name, characters=characters, category=category,
                                         image=image, quantity=quantity, price=price, discount=discount)
        
        pr_qrcode = qrcode.make(f'http://192.168.43.46/product_single/{product.id}/')
        pr_qrcode.save(f'media/d_pr_qrcodes/{product.id}.jpg')
        
        return redirect('add_discount__product')
    
    







def cart(request):
    categories = Category.objects.all()[:8]
    logo = Site_logo.objects.last()
    
    
    context = {
        'categories': categories,
        'logo': logo
    }
    return render(request, 'cart.html', context)





def qrcodes(request):
    products = Product.objects.all()
    d_products = Product_discount.objects.all()
    
    
    context = {
        'products': products,
        'd_products': d_products,
    }
    return render(request, 'qrcodes.html', context)



def category(request, id):
    categories = Category.objects.all()[:8]
    product = Product.objects.filter(category_id=id)
    logo = Site_logo.objects.last()
    
    if product.count() == 0:
        messages.info(request, 'Nothing found on your request')
    context = {
        'product': product,
        'categories': categories,
        'logo': logo,
    }
        
    return render(request, 'filtered_items.html', context)