from django.urls import path
from . views import *

urlpatterns = [
    path('',home),
    path('createblog',createblog),
    path('ulogin',ulogin),
    path('logout',logout),
    path('usignup',signup),
    path('register',register.as_view()),
    path('editpost',editpost),
    path('deletepost',deletepost),
    path('editcomment',editcomment),
    path('deletecomment',deletecomment)

]
