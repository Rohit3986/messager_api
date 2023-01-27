from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Messages(models.Model):
    message = models.TextField()
    total_likes = models.IntegerField(default=0)
    sender = models.ForeignKey(to=User,related_name='sender',on_delete=models.CASCADE)
    recorded_time = models.DateTimeField(auto_now_add=True)

class Likes(models.Model):
    message = models.ForeignKey(to=Messages,on_delete=models.CASCADE)
    like_status = models.CharField(max_length=1,choices=((0,0),(1,1)))
    user = models.ForeignKey(to=User,related_name='user',on_delete=models.CASCADE)
    recorded_time = models.DateTimeField(auto_now_add=True)