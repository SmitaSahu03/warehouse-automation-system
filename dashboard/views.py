from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .models import Rack
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,RackForm
 
# Create your views here.
@login_required()
def index(request):
    return render(request,'dashboard/index.html')

@login_required()
def staff(request):
    
    return render(request,'dashboard/staff.html')

@login_required()
def product(request):
    items = Product.objects.all()
    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')

    else:
        form = ProductForm()  
    context ={
        'items': items,
        'form': form,
    }
    return render(request,'dashboard/product.html',context)

@login_required() 
def rack(request):
    #isle = Rack.objects.all()
    isles = Rack.objects.raw('SELECT * FROM dashboard_rack')
    if request.method == "POST":
        form = RackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-rack')
    else:
        form = RackForm()
    context1 ={
        'isles': isles,
        'form':form
    }
    return render(request,'dashboard/rack.html',context1)

def product_delete(request , pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
       form = ProductForm(request.POST,instance = item)
       if form.is_valid():
        form.save()
        return redirect('dashboard-product')
    else:
        form = ProductForm(instance = item)
        
    context={
        'form':form,

    }
    return render(request,'dashboard/product_update.html',context)