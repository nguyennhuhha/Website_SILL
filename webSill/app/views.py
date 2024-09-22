from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.forms import forms
import os
import json
from django.conf import settings
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def base(request):
    '''
    Trả về base (header & footer)
    '''
    context={}
    return render(request, 'app/base.html',context) 

def home(request):
    """
        Trả về trang chủ home
    """
    collections = Collection.objects.filter()
    context ={'collections':collections}
    return render(request,'app/home.html',context)

def TwoD(request):
    """
        Trả về trang 2D
    """
    collections = Collection.objects.filter(IDtype='2D')
    context ={'collections':collections}
    return render(request,'app/2D.html',context)

def ThreeD(request):
    """
        Trả về trang 3D
    """
    collections = Collection.objects.filter(IDtype='3D')
    context ={'collections':collections}
    return render(request,'app/3D.html',context)

def Icon(request):
    """
        Trả về trang Icon
    """
    collections = Collection.objects.filter(IDtype='Icon')
    context ={'collections':collections}
    return render(request,'app/Icon.html',context)

def About(request):
    """
        Trả về trang About
    """
    context ={}
    return render(request,'app/About.html',context)

def Contact(request):
    """
        Trả về trang Contact
    """
    context ={}
    return render(request,'app/Contact.html',context)

def collection(request):
    """
        Trả về trang sản phẩm collection
    """
    id = request.GET.get('id','')
    collection = Collection.objects.filter(ID=id)
    # collection_id = Collection.objects.get()
    # download = Download(customer=request.user, collection=collection_id)
    # download.save()
    context ={'collection':collection}
    return render(request,'app/collection.html',context)

def updateDownload(request):
    data = json.loads(request.body)
    productId= data['productId']
    action = data['action']
    customer = request.user
    product = Collection.objects.get(ID = productId)
    download, created = Download.objects.get_or_create(customer = customer, collection=product)
    download.save()
    return JsonResponse('added',safe=False)

def search(request):
    """
        Trả về trang kết quả tìm kiếm
    """
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Collection.objects.filter(Name__contains = searched)
    return render(request,'app/search.html',{"searched":searched,"keys":keys})

def register(request):
    """
        Trả về trang đăng kí
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context ={'form':form}
    form.fields['username'].widget.attrs['placeholder'] = 'User name'
    form.fields['email'].widget.attrs['placeholder'] = 'Email'
    form.fields['password1'].widget.attrs['placeholder'] = 'Password'
    form.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
    return render(request,'app/register.html',context)

def Signin(request):
    """
        Trả về trang đăng nhập
    """
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request, 'Wrong password or username!')
    context ={}
    return render(request,'app/signin.html',context)

def logoutuser(request):
    
    '''
    Trả về trang đăng nhập
    '''
    logout(request)
    return redirect('home')