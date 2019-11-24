from django.db import models
from datetime import datetime

# Create your models here.


class Host(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name = models.CharField(max_length=200,)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    visiting_host = models.ForeignKey(Host,default=1,on_delete=models.SET_DEFAULT)
    checkin_time = models.DateTimeField("time arrived",default=datetime.now())
    checkout_time = models.TimeField("time leaving",blank=True, null=True)

    def checkin(self):
        self.checkin_time = datetime.now();
        self.save();
    
    def checkout(self):
        self.checkout_time = datetime.now()
        self.save();
    
    def __str__(self):
        return self.name


