from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('',home),
    path('createblog',createblog),
    path('detailblog/<bid>',detailblog),
    path('ulogin',ulogin),
    path('logout',logoutt),
    path('usignup',signup),
    path('register',register.as_view()),
    path('editpost',editpost),
    path('deletepost',deletepost),
    path('editcomment',editcomment),
    path('deletecomment',deletecomment)

]
