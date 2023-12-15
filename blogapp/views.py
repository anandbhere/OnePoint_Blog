from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import *
from django.views import View
from .models import Posts,Comments


# Create your views here.
def home(request):
    context = {}
    id = request.user.id
    blog = Posts.objects.all()
    comments = Comments.objects.all()
    print(blog)
    print(request.user.username)
    #print(comments)
    context['blogpost'] = blog
    #context['comments'] = comments
    return render(request,'home.html',context)


def createblog(request):
    context={}
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,'createblog.html')
        else:
            title = request.POST['posttitle']
            bpost = request.POST['posttext']
            u_obj = User.objects.get(id = request.user.id)
            b = Posts.objects.create(title = title, post = bpost,uid = u_obj)
            b.save()
            print(u_obj)
            context['msg'] = 'New Blog Added successfully'
            return render(request,'createblog.html',context )
    else:
        return redirect('/ulogin')


def detailblog(request,bid):
    context = {}
    b_details = Posts.objects.get(id=bid)
    context['blog_details'] = b_details
    print(b_details)
    print(b_details.title)
    return render(request,'detailblog.html',context)


def ulogin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        context={}
        uname=request.POST['username']
        upass=request.POST['password']
 
        if uname=='' or upass=='':
            context['err']='username and password required'
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/')
            
            else:
                context['err']='invalid username and password'
                return render(request,'login.html',context)

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
        uemail = request.POST['uemail']
        password = request.POST['password']
        cpass = request.POST['cpass']
        print(name)
        print(uemail)
        print(password)
        print(cpass)
        context ={}
        if password != cpass:
            context['err']= 'Password and confirm password did not match'
            return render(request,"register.html",context)
        else:
             u = User.objects.create(username = name,email=uemail)
             u.set_password(password)
             u.save()
             context['err']= 'Successfully registered Please Login'

             return render(request,'register.html',context)

    


def logoutt(request):
    logout(request)
    return redirect('/')


def editpost(request):
    return render(request,'home.html',{})


def deletepost(request):
    return render(request,'home.html',{})

def editcomment(request):
    return render(request,'editcomment.html',{})

def deletecomment(request):
    return render(request,'home.html',{})