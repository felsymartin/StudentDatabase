from django.shortcuts import render
from django.contrib.auth.models import User,auth

# Create your views here.

def index(request):
    return render (request,'adminlogin.html')

def login(request):
    uname=request.POST['uname']
    psw=request.POST['psw']
    user = auth.authenticate(username=uname,password=psw)
    if user is not None:
        return render(request,'success.html')
    else:
        msg='Invalid username or password!!!'
        return render(request,'adminlogin.html',{'lmsg':msg})