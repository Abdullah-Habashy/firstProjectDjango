from django.shortcuts import render

# written in views file inside app
from .models import Product
# import the target model "Product" from models


def product(request):
    data = Product.objects.all()
    # receive all data from that model
    return render(request, 'products/product.html', {"data": data})
    # pass data to target file
    
def products(request):
    data = Product.objects.all()
    # receive all data from that model
    return render(request, 'products/products.html', {"data": data})
    # pass data to target file




# folderOfAppInsideTemplates/filename.html
