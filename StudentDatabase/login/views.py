from django.shortcuts import render
from django.contrib.auth.models import User,auth

from login.models import student_details

# Create your views here.

def index(request):
    return render (request,'adminlogin.html')

def login(request):
    uname=request.POST['uname']
    psw=request.POST['psw']
    user = auth.authenticate(username=uname,password=psw)
    if user is not None:
        return render(request,'datahome.html')
    else:
        msg='Invalid username or password!!!'
        return render(request,'adminlogin.html',{'lmsg':msg})

def register(request):

    if request.method == 'POST':
        sname = request.POST['name']
        sad_no = request.POST['Adnumb']
        scourse = request.POST['course']
        sgender = request.POST['Gender']
        sage = request.POST['Age']
        saddress = request.POST['Address']

        student = student_details.objects.create(name = sname, ad_no = sad_no, course = scourse, age = sage, gender = sgender, address = saddress)
        student.save();

        successmsg = 'Successfully Registered'
    
        return render(request,'studentregistration.html',{'success':successmsg})

    else:
        return render(request,'studentregistration.html')