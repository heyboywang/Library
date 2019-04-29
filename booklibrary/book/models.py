from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suser(User):
    college = models.CharField(max_length=30,null=True,blank=True)
    uno = models.IntegerField(null=True,blank=True)

class Book(models.Model):
    bname = models.CharField(max_length=255)
    auther = models.CharField(max_length=20)
    public_com = models.CharField(max_length=255,null=True,blank=True)
    public_date = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.bname

class Borrows(models.Model):
    uname = models.ForeignKey(User,on_delete=models.CASCADE)
    bname = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_borrow = models.DateTimeField(auto_now_add=True)
    date_retur = models.DateTimeField()
    status = models.BooleanField(default=False)

    def statu(self):
        return self.status
    statu.short_description = '状态'

