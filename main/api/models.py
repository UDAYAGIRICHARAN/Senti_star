from django.db import models
from django.contrib.auth.models import User
#django.db.models.JSONField
from django.db.models import JSONField
# Create your models here.
class Image(models.Model):
    userid=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    datatime=models.DateTimeField(auto_now_add=True)
    imageName=models.CharField(max_length=100)

class Audio(models.Model):
    userid=models.CharField(max_length=100)
    audio=models.FileField(upload_to='audios/')
    datatime=models.DateTimeField(auto_now_add=True)
    audioName=models.CharField(max_length=100)
class Url(models.Model):
    userid=models.CharField(max_length=100)
    url=models.CharField(max_length=500)
    datatime=models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    
    userid=models.CharField(max_length=100)
    responsedata=JSONField()
    datatime=models.DateTimeField(auto_now_add=True)
    service=models.CharField(max_length=100)
    servicepaths=JSONField()
    serviceLocation=JSONField()
    



    def __str__(self):
        return self.userid
class Files(models.Model):
    userid=models.CharField(max_length=100)
    files=models.FileField(upload_to='files/')
    datatime=models.DateTimeField(auto_now_add=True)
    filetype=models.CharField(max_length=100)
    fileName=models.CharField(max_length=100)
    def __str__(self):
        return self.userid















# class Image(models.Model):

    # def __str__(self):
    #     return self.image