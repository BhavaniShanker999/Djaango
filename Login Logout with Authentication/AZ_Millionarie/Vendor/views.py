from django.shortcuts import render,redirect
from Vendor.models import Vendormod
from django.contrib.auth.decorators import login_required
from Vendor.forms import insert_new_vendorform,signupform
from django.http import HttpResponseRedirect

# Create your views here.
def view1(request):
    data_list=Vendormod.objects.all()
    return render(request,'Vendor/Vendor.html',{'data_list':data_list})

def home_view(request):
    return render(request,'Vendor/welcome.html')

def luckywinners_view(request):
    return render(request,'Vendor/luckywinners.html')

def successcustomers_view(request):
    return render(request,'Vendor/successcustomers.html')

@login_required
def happystories_view(request):
    return render(request,'Vendor/happystories.html')


def login_view(request):
    return render(request,'Vendor/logen.html')

def signup_view(request):
    form=signupform()
    if request.method=="POST":
            form=signupform(request.POST)
            if form.is_valid():
                user=form.save()
                user.set_password(user.password)
                user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'Vendor/signup.html',{'form':form})

def retrivevendor_view(request):
    vendors_list=Vendormod.objects.all()
    return render(request,'vendor_crud/retrive_vendor.html',{'vendors_list':vendors_list})

def insert_new_vendor_view(request):
    form=insert_new_vendorform()
    if request.method=="POST":
        form=insert_new_vendorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vendor_list')
    return render(request,'vendor_crud/insert_new_vendor.html',{'form':form})

def delete_vendor_view(request,id):
    delete_vendor=Vendormod.objects.get(id=id)
    delete_vendor.delete()
    return redirect('/vendor_list')
