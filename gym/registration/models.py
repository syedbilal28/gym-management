from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_init, post_save, pre_save
# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        ordering=("price",)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    cnic=models.CharField(max_length=15,null=True,blank=True)
    phone=models.CharField(max_length=11,null=True,blank=True)
    fingerprint=models.CharField(max_length=100,null=True,blank=True)    
    package=models.ForeignKey(Service,on_delete=models.CASCADE)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
class Attendance(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + self.timestamp 

class Payment(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + self.timestamp
    


