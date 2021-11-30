from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django import forms
from travello.forms import UserForm
import os

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def destinations(request):
    return render(request,'destinations.html')
def register(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"this username already exists")
                # return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already used")
                # return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                messages.info(request,"User Created")
                return redirect('login')
        else:
            messages.info(request,"password is not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    else:
        return render(request,'login.html')
