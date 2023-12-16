from django.db import models
from django.contrib.auth.models import User
import datetime





class Posts(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='postimages',blank = True, null = True)
    shortdesc = models.CharField(max_length=200)
    description =  models.CharField(max_length=600)
    created_on = models.DateField(default = datetime.date.today)



class Comments(models.Model):
    post = models.ForeignKey(Posts,on_delete = models.CASCADE,db_column = 'post')
    commented_by = models.ForeignKey(User,on_delete = models.CASCADE, db_column = 'commented_by' )
    text = models.CharField(max_length = 254)
    name = models.CharField(max_length = 200)