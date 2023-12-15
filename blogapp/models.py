from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.


print(timezone.now)
print(timezone.now())



class Posts(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Posts')
    shortdesc = models.CharField(max_length=200)
    description =  models.TextField()
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    created_on = models.DateField(default = datetime.date.today)



class Comments(models.Model):
    #id = User.objects.get(id)
    comment = models.CharField(max_length=254)
    created_by = models.ForeignKey(Posts.id)
