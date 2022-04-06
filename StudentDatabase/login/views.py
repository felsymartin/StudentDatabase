from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.http import HttpResponse, JsonResponse
from django.db.models.query_utils import Q


from login.models import student_details

# Create your views here.

def index(request):
    return render (request,'adminlogin.html')

def login(request):
    uname=request.POST['uname']
    psw=request.POST['psw']
    user = auth.authenticate(username=uname,password=psw)
    if user is not None:
        stdlist = student_details.objects.all()
        return render(request,'datahome1.html', {'course':stdlist})
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


def detailsview(request,btch):
    if btch == 1:
   
        course = student_details.objects.filter(course='Science')
    elif btch ==2:
        course = student_details.objects.filter(course='Commerce')
    else:
        course = student_details.objects.filter(course='Humanities')
    return render (request,'datahome1.html', {'course':course})
    #return redirect('/detailsview/')


def idview(request):
    if 'search' in request.GET:
        search = request.GET['search']
        data = student_details.objects.filter(ad_no=search)
    else:
        data = student_details.objects.all()
    context = {
            'data' : data
        }
    return render (request,'search_1.html', context)