from django.shortcuts import render,redirect
from .models import product
from .forms import CreateProductForm

# Create your views here.
def list_products(request):
    products= product.objects.all()
    return render(request,'all-temps/products.html',{'products':products})
    

def create_products(request):
    form =CreateProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all-products') 
    else:
        form =CreateProductForm ()
    return render(request,'all-temps/products-form.html',{"form":form})

def update_products(request,id):
    products=product.objects.get(id=id)
    
    form =CreateProductForm(request.POST or None ,instance=products)
    if form.is_valid():
        form.save()
        return redirect('all-products') 
    else:
        form =CreateProductForm ()
    return render(request,'all-temps/products-form.html',{"form":form,'products':products})

def delete_products(request,id):
    products=product.objects.get(id=id)

    if request.method=='POST':
        
        products.delete()
        return redirect('all-products')
    return render(request,'all-temps/prod_delete_confirm.html',{'products':products})

