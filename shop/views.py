from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from shop.form import CustomForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.messages.api import success
import json

def home(request):
    products=Product.objects.filter(trending=1)
    catagory=Catagory.objects.filter(status=0)

    return render(request,'index.html',{'products':products,'catagory':catagory})
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
        return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            psw=request.POST.get('password')
            user=authenticate(request,username=name,password=psw)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect('/')
            else:
                messages.warning(request,"Invalid Username or Password")
                return redirect("/login")
        return render(request,'login.html')

def register(request):
    form=CustomForm()
    if request.method=='POST':
        form=CustomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successfully..!")
            return redirect('/login')
    return render(request,'register.html',{'form':form})

def collection(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'collection.html',{"catagory":catagory})


def collectionView(request,name):
    if (Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(catagory__name=name)
        return render(request,'shop/products/product.html',{"products":products,"category_name":name})
    else:
        messages.warning(request,"No record found")
        return redirect('collection')
    
def product_details(request,cname,pname):
    if (Catagory.objects.filter(name=cname,status=0)):
        if (Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{'products':products})
        else:
            messages.error(request,"No products found")
            return redirect('collection')
    else:
        messages.error(request,"No categories found")
        return redirect('collection')

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHTTpRequest':
    if request.user.is_authenticated:
        data=json.load(request)
        product_qty=data['product_qty']
        product_id=data['pid']
        # print(request.user.id)
        product_status=Product.objects.get(id=product_id)
        if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status': 'Product Already in Card'}, status=200)
            else:
                if product_status.quality>=product_qty:
                    Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                    return JsonResponse({'status':'Product Added to Cart'}, status=200)
                else:
                    return JsonResponse({'status':'Product Out of Stock'}, status=200)
    else:
     return JsonResponse({'status':'Login to add Cart'}, status=200)
   else:
    return JsonResponse({'status': 'Invalid Access'}, status=200)   


def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,'cart.html',{'cart':cart})
    else:
        return redirect('/')
    

def favview_page(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,'fav.html',{'fav':fav})
    else:
        return redirect('/')

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cart')

def remove_fav(request,fid):
    favitem=Favourite.objects.get(id=fid)
    favitem.delete()
    return redirect('/favview_page')

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHTTpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status': 'Product Already in Favourite'}, status=200)
                else:
                    Favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product added to Favourtie'}, status=200)
        else:
                return JsonResponse({'status':"Login to add Favourites"},status=200)
    else:
        return JsonResponse({'status':"Invalid Details"},status=200) 
    