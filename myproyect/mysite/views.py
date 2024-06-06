from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
        return render(request, 'mysite/add_product.html', {'form': form})
    
def index(request):
    products = Product.objects.all()
    return render(request, 'mysite/index.html', {'products': products})
