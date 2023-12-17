from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import *
from django.views import View
import os


# Create your views here.
def home(request):
    context = {}
    id = request.user.id
    blog = Posts.objects.all()
    c_details = Comments.objects.all()
    context['comments'] = c_details
    
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
            description = request.POST['description']
            shortdesc = request.POST['shortdesc']
            u_obj = User.objects.get(id = request.user.id)
            img = request.FILES['img']
            b = Posts.objects.create(uid = u_obj,title = title,img = img, shortdesc = shortdesc, description = description,)
            b.save()
            context['msg'] = 'New Blog Added successfully'
            return render(request,'createblog.html',context )
    else:
        return redirect('/ulogin')


def detailblog(request,bid):
    context = {}
    b_details = Posts.objects.get(id=bid)
    context['blog_details'] = b_details
    c_details = Comments.objects.filter(post=bid)
    context['comments'] = c_details
    print(c_details)
    #print(b_details.title)
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST['comment']
            name = request.user.username
            commented_by = User.objects.get(id=request.user.id)
            c = Comments.objects.create(text = text,name = name, post = b_details ,commented_by = commented_by)
            c.save()

            return render(request,'detailblog.html',context)
        else:
            return render(request,'detailblog.html',context)

            
    else:
        context['errmsg'] = 'You must login first to comment'
        return render(request,'detailblog.html',context)

    return render(request,'detailblog.html',context)
    
def addcomment(request,bid):
    context = {}
    b_details = Posts.objects.get(id=bid)
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST['comment']
            name = request.user.username
            commented_by = User.objects.get(id=request.user.id)
            c = Comments.objects.create(text = text,name = name, post = b_details ,commented_by = commented_by)
            c.save()

            return render(request,'detailblog.html',context)
        else:
            return render(request,'detailblog.html',context)

            
    else:
        return redirect('/detailblog')
        # context['errmsg'] = 'You must login first to comment'
        # return render(request,'detailblog.html',context)





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


def editpost(request,id):
    context = {}
    if request.user.is_authenticated:
        if request.method =='GET':
            p = Posts.objects.filter(id=id)
            context['posts'] = p
            return render(request,'editpost.html',context)
        else:
            title = request.POST['posttitle']
            description = request.POST['description']
            shortdesc = request.POST['shortdesc']
            u_obj = User.objects.get(id = request.user.id)
            if title == '' or description =='' or shortdesc =='' :
                context['errmsg'] = 'Fields cannot be empty'
                return render(request,'editpost.html')
            else:
                post = Posts.objects.filter(id=id)
                post.update(uid = u_obj,title = title,shortdesc = shortdesc, description = description,)
                
                p_img = Posts.objects.get(id =id)
                 
                
                try:
                    if len(request.FILES) != 0:
                        if len(p_img.img) > 0 :
                            os.remove(p_img.img.path)
                    p_img = request.FILES['img']
                    print(p_img)
                    
                except:
                    context['posts'] = post
                    context['errmsg']= 'Fields Cannot be empty'
                    #return render(request,'editpost.html',context)
                p_img.save(p_img.img.path)
            
           

            context['msg'] = 'New Blog Edited successfully'
            #return render(request,'editblog.html',context)
            return redirect('/')


    else:
        return redirect('/ulogin')



def deletepost(request,id):
    context = {}
    if request.user.is_authenticated:
        did = Posts.objects.get(id = id)
        did.delete()
        return redirect('/')
        

    else:
        context['errmsg']="You must login first"
        return render(request,'detailblog.html',context)

def editcomment(request):
    return render(request,'editcomment.html',{})

def deletecomment(request):
    return render(request,'home.html',{})