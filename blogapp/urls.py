from django.urls import path
from blogapp.views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home),
    path('createblog',createblog),
    path('detailblog/<bid>',detailblog),
    path('ulogin',ulogin),
    path('logout',logoutt),
    path('usignup',signup),
    path('register',register.as_view()),
    path('editpost/<id>',editpost),
    path('deletepost/<id>',deletepost),
    path('editcomment',editcomment),
    path('deletecomment',deletecomment),
    path('addcomment/<bid>',addcomment),
    
]+  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

''' or we can write this media settings in following ways also after urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA,document_root=settings.MEDIA_ROOT)

'''