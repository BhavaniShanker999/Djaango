from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from accounts.models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm


def login(request):
    context={}
    return render(request,'accounts/login.html',context)


def register(request):
    form=UserCreationForm
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def home(request):
    customers_info=customer_model.objects.all()
    orders_info=order_model.objects.all()
    total_customers=customers_info.count()
    total_orders=orders_info.count()
    pending=orders_info.exclude(status='Delivered').count()
    delivered=orders_info.filter(status='Delivered').count()

    context={'customers_info':customers_info,'orders_info':orders_info,
             'total_customers': total_customers, 'total_orders': total_orders,
             'pending': pending, 'delivered': delivered}

    return render(request,'accounts/dashboard.html',context)

def products(request):
    products_info=Product_model.objects.all()
    context={'products_info':products_info}
    return render(request,'accounts/products.html',context)

def customer(request,keyy):
    customer=customer_model.objects.get(id=keyy)
    orders=customer.order_model_set.all()
    orders_count=orders.count()
    myfilter=order_filter(request.GET,queryset=orders)
    orders=myfilter.qs
    context = {'customer': customer, 'orders': orders,
               'orders_count': orders_count,'myfilter':myfilter}
    return render(request,'accounts/customer.html',context)

def create_order(request, keyy):
    create_order_formset=inlineformset_factory(customer_model,order_model,fields=('products_mod','status'))
    customer_mod =customer_model.objects.get(id=keyy)
    formset = create_order_formset(instance=customer_mod)
    if request.method == 'POST':
        formset = create_order_formset(request.POST,instance=customer_mod)
        
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'accounts/create_order.html',context)


def add_product(request):
    form=add_product_form()
    if request.method=='POST':
        form=add_product_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context={'form':form}
    return render(request,'accounts/add_product.html',context)


def update_order(request,pk):
    order=order_model.objects.get(id=pk)
    form=create_order_form(instance=order)
    if request.method == 'POST':
        form = create_order_form(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/update_order.html',context)

def delete_order(request,pk):
    order=order_model.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
     
    context = {'order': order}
    return render(request,'accounts/delete_order.html',context)

