from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Product,OrderItems,Orders
from  .form import ProductForm
from django.contrib import messages



# Create your views here.

class ProductIndex(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'product_list'
    def get_queryset(self):
        return Product.objects.order_by('-name')[:5]

def product_details(request,prod_id):
    product = get_object_or_404(Product,pk=prod_id)
    return render(request,'products/product_detail.html',{'prod':product})

def add_to_cart(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            prod_id = form.cleaned_data['prod_id']
            prod_name = form.cleaned_data['prod_name']
            prod_price = form.cleaned_data['prod_price']
            quantity = form.cleaned_data['quantity']
            q= Product.objects.get(pk = prod_id)

            if q.stock < quantity:

                context = messages.error(request,'Stock is not sufficient.')
            else:
                amount = int(prod_price)*quantity
                q.stock = q.stock- quantity
                q.save()
                request.session[prod_id] = [prod_name,quantity,amount]
                context = {
                    'prod_name':prod_name,
                    'quantity':quantity,
                    'amount':float(amount),
                }
        else:
            form = ProductForm()
    return render(request,'products/addtocart.html',context)




