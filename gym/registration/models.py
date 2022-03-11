from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        ordering=("price",)
class Member(models.Model):
    identity=models.CharField(max_length=10,null=True)
    name=models.CharField(max_length=256)
    cnic=models.CharField(max_length=15,null=True,blank=True)
    phone=models.CharField(max_length=11,null=True,blank=True)
    fingerprint=models.CharField(max_length=100,null=True,blank=True)    
    package=models.ForeignKey(Service,on_delete=models.CASCADE)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.name
@receiver(post_save,sender=Member)
def MemberIdHandler(sender,instance,created, **kwargs):
    if created:
        instance.identity=f"FP{instance.id:04d}"
        instance.save()
class Attendance(models.Model):
    user=models.ForeignKey(Member,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + self.timestamp 

class Payment(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + self.timestamp
    


