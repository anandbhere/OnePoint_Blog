from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import *
from django.views import View

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def createblog(request):
    return render(request,'createblog.html')


def ulogin(request):
    return render(request,'login.html')

def signup(request):
    # if request.method == "GET":
    #     return render(request,'signup.html')
    # else:

    #     name = request.POST['name']
    #     email = request.POST['uemail']
    #     password = request.POST['password']
    #     cpassword = request.POST['cpassword']
    #     u = User.objects.create(username = name)
    #     u.set_password(password)
    #     u.save()
    #     print(name,email,password)
    #     return render(request,'signup.html',{'context':'Signed up successfully, please login..!!'})
    
    
    # context = {}
    # if request.method=="GET":

    #     return render(request,'signup.html')
    # else:
    #     #fetch and store form data
    #     uname = request.POST['uname']
    #     uemail = request.POST['uemail']
    #     upass = request.POST['upass']
    #     ucpass = request.POST['ucpass']

    #     # validation
    #     if uname =='' or uemail == '' or upass =='' or ucpass == '':
    #         context['errmsg'] = "Fields cannot be empty"
    #         return render(request,'signup.html', context)

    #     elif upass != ucpass :
    #         context['errmsg'] = "Password and Confirm Password Missmatch"
    #         return render(request,'signup.html', context)

    #     elif len(upass)<8 :
    #         context['errmsg'] = "Password is less than 8 characters "
    #         return render(request,'signup.html', context)
            
    #     elif upass.isdigit():
    #         context['errmsg'] = "Password should not numeric entirely   "
    #         return render(request,'signup.html', context)    
    #     else:
    #         u = User.objects.create(username = uname, email = uemail )
    #         u.set_password(upass)
    #         u.save()
    #         context['Success'] = "User created successfully"
    return render(request,'signup.html')

class register(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST["cpass"]
         
        u = User.objects.create(username = name)
        u.set_password(password)
        u.save()
        return render(request,"register.html",{'msg':'Successfully registered Please Login'})

    


def logout(request):
    return render(request,'home.html')


def editpost(request):
    return render(request,'home.html',{})


def deletepost(request):
    return render(request,'home.html',{})

def editcomment(request):
    return render(request,'editcomment.html',{})

def deletecomment(request):
    return render(request,'home.html',{})